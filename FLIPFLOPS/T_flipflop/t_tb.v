// Testbench for T Flip-Flop with VCD generation
module tb_t_flipflop;
    // Signals for T Flip-Flop
    reg T, clk, rst;
    wire Q, Qn;

    // Instantiate the T Flip-Flop
    t_flipflop uut (
        .T(T),
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
        T = 0;

        // Open VCD file
        $dumpfile("t_waveform.vcd");
        $dumpvars(0, tb_t_flipflop);

        // Apply reset
        rst = 1; #10;
        rst = 0; #10;

        // Test T Flip-Flop behavior
        T = 1; #20; // Toggle Q
        T = 0; #20; // No change
        T = 1; #20; // Toggle Q again

        // Finish the simulation
        $finish;
    end
endmodule
