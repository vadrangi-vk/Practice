// JK Flip-Flop Module
module jk_flipflop (
    input J,        // Input J
    input K,        // Input K
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
            case ({J, K})
                2'b00: begin
                    Q <= Q;
                    Qn <= Qn;
                end
                2'b01: begin
                    Q <= 0;
                    Qn <= 1;
                end
                2'b10: begin
                    Q <= 1;
                    Qn <= 0;
                end
                2'b11: begin
                    Q <= ~Q;
                    Qn <= ~Qn;
                end
            endcase
        end
    end
endmodule
