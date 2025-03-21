// Testbench for JK Flip-Flop with VCD generation
module tb_jk_flipflop;
    // Signals for JK Flip-Flop
    reg J, K, clk, rst;
    wire Q, Qn;

    // Instantiate the JK Flip-Flop
    jk_flipflop uut (
        .J(J),
        .K(K),
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
        J = 0;
        K = 0;

        // Open VCD file
        $dumpfile("jk_waveform.vcd");
        $dumpvars(0, tb_jk_flipflop);

        // Apply reset
        rst = 1; #10;
        rst = 0; #10;

        // Test JK Flip-Flop behavior
        J = 1; K = 0; #20; // Set J=1, K=0
        J = 0; K = 1; #20; // Set J=0, K=1
        J = 1; K = 1; #20; // Set J=1, K=1
        J = 0; K = 0; #20; // Set J=0, K=0

        // Finish the simulation
        $finish;
    end
endmodule
