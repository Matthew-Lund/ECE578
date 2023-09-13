`timescale 1ps/1ns

module lfsr (
    input [9:0] initial,
    input clk, reset,
    output [511:0] bitstream
);
    reg [9:0] state = initial;
    assign bitsteam[511] = state[0]; //Done so initial bit is kept in first out of bitstream
    always @(posedge clk or negedge reset)
        begin
            if(!reset) begin
                state <= initial;
                bitstream <= 512'd0;
            end
            else
            begin
                for(int i = 0; i <= 511; i++)begin
                    state <= {state[8:0], state[9] ^ state[5] ^ state[4] ^ state[3] ^ state[0]};
                    // Feedback polynomial: x^10 + x^8 + x^3 + x^2 + 1
                    bitstream[510-i] <= state[0];//Assign bitstream point to state value leaving
                end
            end
        end
endmodule