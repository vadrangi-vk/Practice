// D Flip-Flop Module
module d_flipflop (
    input D,        // Input D
    input clk,      // Clock input
    input rst,      // Asynchronous Reset
    output reg Q,   // Output Q
    output reg Qn   // Output Qn (Q not)
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            Q <= 0;
            Qn <= 1;
        end else begin
            Q <= D;
            Qn <= ~D;
        end
    end
endmodule
