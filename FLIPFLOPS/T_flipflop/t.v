// T Flip-Flop Module
module t_flipflop (
    input T,        // Toggle input
    input clk,      // Clock input
    input rst,      // Asynchronous reset
    output reg Q,   // Output Q
    output reg Qn   // Output Qn (Q not)
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            Q <= 0;
            Qn <= 1;
        end else begin
            if (T) begin
                Q <= ~Q;    // Toggle Q
                Qn <= ~Qn;  // Toggle Qn
            end
        end
    end
endmodule
