// RS Flip-Flop Module
module rs_flipflop (
    input R,        // Reset input
    input S,        // Set input
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
            case ({S, R})
                2'b00: begin
                    Q <= Q;    // No change
                    Qn <= Qn;
                end
                2'b01: begin
                    Q <= 0;    // Reset Q
                    Qn <= 1;
                end
                2'b10: begin
                    Q <= 1;    // Set Q
                    Qn <= 0;
                end
                2'b11: begin
                    Q <= 1;    // Invalid state in RS Flip-Flop, but can be treated as set
                    Qn <= 0;
                end
            endcase
        end
    end
endmodule
