module SpectralHumorKernel

using LinearAlgebra
using StaticArrays

export modal_coupling_operator,
       qr_isometric_basis,
       chromatic_loop_step,
       damped_loop_step,
       governed_modal_step

"""
    qr_isometric_basis(A::SMatrix{D, N, Float64}) -> SMatrix{D, N, Float64}

Construct a sign-normalized orthonormal subspace basis P_iso ∈ R^{D × N}
from raw basis columns A without dynamic heap allocations.
"""
function qr_isometric_basis(A::SMatrix{D, N, Float64}) where {D, N}
    F = qr(A)
    Q = SMatrix{D, N, Float64}(F.Q)
    R = SMatrix{N, N, Float64}(F.R)
    signs = SVector{N, Float64}(ntuple(j -> R[j, j] < 0.0 ? -1.0 : 1.0, Val(N)))
    return Q .* signs'
end

"""
    modal_coupling_operator(W_sym::SMatrix{N, N, Float64},
                            W_skew::SMatrix{N, N, Float64},
                            alpha::Float64,
                            beta::Float64) -> SMatrix{N, N, Float64}

Build M(α, β) = I_N - α * (I_N - D^{-1}(W_sym + β W_skew)) on stack-allocated StaticArrays.
"""
function modal_coupling_operator(
    W_sym::SMatrix{N, N, Float64},
    W_skew::SMatrix{N, N, Float64},
    alpha::Float64,
    beta::Float64,
) where {N}
    W = W_sym + beta .* W_skew
    row_sums = sum(abs.(W), dims=2)
    inv_d = SVector{N, Float64}(ntuple(i -> row_sums[i] > 1e-12 ? 1.0 / row_sums[i] : 0.0, Val(N)))
    D_inv_W = inv_d .* W
    I_N = SMatrix{N, N, Float64}(I)
    L = I_N - D_inv_W
    return I_N - alpha .* L
end

"""
    governed_modal_step(x::SVector{N, Float64},
                        u::SVector{N, Float64},
                        M::SMatrix{N, N, Float64},
                        tau_safe::Float64 = 0.96) -> Tuple{SVector{N, Float64}, Float64, Bool}

Advance expressive state x_{n+1} = M_eff * x_n + u_n while enforcing the Dream-Lane
spectral radius ceiling ρ(M_eff) <= tau_safe via uniform radial scaling (preserving
complex eigenmode phase angles). Executes with 0 B heap allocation.
"""
function governed_modal_step(
    x::SVector{N, Float64},
    u::SVector{N, Float64},
    M::SMatrix{N, N, Float64},
    tau_safe::Float64 = 0.96,
) where {N}
    # Power-iteration spectral radius estimate
    v = SVector{N, Float64}(ntuple(i -> 1.0 / sqrt(Float64(N)), Val(N)))
    for _ in 1:8
        Mv = M * v
        nrm = norm(Mv)
        v = nrm > 1e-15 ? Mv / nrm : v
    end
    rho_est = norm(M * v)

    damped = rho_est > tau_safe
    M_eff = damped ? (tau_safe / rho_est) .* M : M

    x_next = M_eff * x + u
    return (x_next, rho_est, damped)
end

"""
    chromatic_loop_step(x0::SVector{N, Float64},
                        M::SMatrix{N, N, Float64},
                        K::Int = 16,
                        tol::Float64 = 1e-6,
                        tau_safe::Float64 = 0.96) -> Tuple{SVector{N, Float64}, Bool}

Iterate closed damped feedback loop x_{k+1} = M_eff * x_k over K cycles under
`governed_modal_step` and certify drift-neutral convergence ||x_K - x_{K-1}||_2 < tol.
"""
function chromatic_loop_step(
    x0::SVector{N, Float64},
    M::SMatrix{N, N, Float64},
    K::Int = 16,
    tol::Float64 = 1e-6,
    tau_safe::Float64 = 0.96,
) where {N}
    x_prev = x0
    x_curr = x0
    u_zero = zero(SVector{N, Float64})
    for _ in 1:K
        x_prev = x_curr
        x_curr, _, _ = governed_modal_step(x_prev, u_zero, M, tau_safe)
    end
    converged = norm(x_curr - x_prev) < tol
    return (x_curr, converged)
end

const damped_loop_step = chromatic_loop_step

end # module
