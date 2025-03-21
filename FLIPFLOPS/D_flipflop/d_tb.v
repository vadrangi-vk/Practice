// Testbench for D Flip-Flop with VCD generation
module tb_d_flipflop;
    // Signals for D Flip-Flop
    reg D, clk, rst;
    wire Q, Qn;

    // Instantiate the D Flip-Flop
    d_flipflop uut (
        .D(D),
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
        D = 0;

        // Open VCD file
        $dumpfile("d_waveform.vcd");
        $dumpvars(0, tb_d_flipflop);

        // Apply reset
        rst = 1; #10;
        rst = 0; #10;

        // Test D Flip-Flop behavior
        D = 1; #20; // Set D=1
        D = 0; #20; // Set D=0

        // Finish the simulation
        $finish;
    end
endmodule
