using Test
using LinearAlgebra
using StaticArrays

include(joinpath(@__DIR__, "..", "src", "SpectralHumorKernel.jl"))
using .SpectralHumorKernel

@testset "SpectralHumorKernel Invariants" begin
    @testset "QR Isometric Basis Machine Precision & Zero Allocation" begin
        A = @SMatrix [
            1.0 0.2;
            0.3 1.1;
            -0.4 0.5;
            0.1 -0.3
        ]
        P_iso = qr_isometric_basis(A)
        @test norm(P_iso' * P_iso - I) < 1e-14

        # Warmup compilation before measuring heap allocations
        qr_isometric_basis(A)
        @test (@allocated qr_isometric_basis(A)) == 0
    end

    @testset "Dream-Lane Spectral Governor & Zero Allocation" begin
        W_sym = @SMatrix [0.0 1.0; 1.0 0.0]
        W_skew = @SMatrix [0.0 1.0; -1.0 0.0]
        M_unstable = modal_coupling_operator(W_sym, W_skew, 0.95, 3.50)

        x = @SVector [1.0, 0.5]
        u = @SVector [0.2, 0.1]

        x_next, rho_est, damped = governed_modal_step(x, u, M_unstable, 0.96)
        @test damped == true
        @test rho_est > 0.96
        @test all(isfinite, x_next)

        # Warmup compilation before measuring heap allocations
        governed_modal_step(x, u, M_unstable, 0.96)
        @test (@allocated governed_modal_step(x, u, M_unstable, 0.96)) == 0
    end

    @testset "Chromatic Loop Convergence" begin
        W_sym = @SMatrix [0.0 1.0; 1.0 0.0]
        W_skew = @SMatrix [0.0 1.0; -1.0 0.0]
        M_stable = modal_coupling_operator(W_sym, W_skew, 0.25, 0.50)

        x0 = @SVector [1.0, -1.0]
        x_final, converged = chromatic_loop_step(x0, M_stable, 64, 1e-5)
        @test converged == true
        @test norm(x_final) < 1e-4
    end
end
