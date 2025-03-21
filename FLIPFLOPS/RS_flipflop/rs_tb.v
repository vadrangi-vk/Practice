// Testbench for RS Flip-Flop with VCD generation
module tb_rs_flipflop;
    // Signals for RS Flip-Flop
    reg R, S, clk, rst;
    wire Q, Qn;

    // Instantiate the RS Flip-Flop
    rs_flipflop uut (
        .R(R),
        .S(S),
        .clk(clk),
        .rst(rst),
        .Q(Q),
        .Qn(Qn)
    );

    // Clock generation
    always begin
        #5 clk = ~clk; // Generate clock with 10-time unit period
    end

    // VCD file generation
    initial begin
        // Initialize signals
        clk = 0;
        rst = 0;
        R = 0;
        S = 0;

        // Open VCD file
        $dumpfile("rs_waveform.vcd");
        $dumpvars(0, tb_rs_flipflop);

        // Apply reset
        rst = 1; #10;
        rst = 0; #10;

        // Test RS Flip-Flop behavior
        S = 1; R = 0; #20; // Set Q
        S = 0; R = 1; #20; // Reset Q
        S = 0; R = 0; #20; // No change
        S = 1; R = 1; #20; // Invalid state (can treat as Set)

        // Finish the simulation
        $finish;
    end
endmodule
