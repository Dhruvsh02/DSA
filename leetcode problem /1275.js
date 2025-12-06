/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function(moves) {
    const rows = [0,0,0]
    const cols = [0,0,0]
    let dia = 0 , antidiag = 0;

    for (let i = 0; i < moves.length ; i++){
        const [r,c] = moves[i];
        const player = (i%2 === 0) ? 1 : -1;

        rows[r] += player;
        cols[c] += player;

        if (r===c) dia += player;
        if (r+c ===2) antidiag += player

        if(Math.abs(rows[r]) === 3 || Math.abs(cols[c]) === 3 || Math.abs(dia) === 3 || Math.abs(antidiag) === 3){
            return player === 1 ? "A" : "B";
        }
    }

    return moves.length === 9 ? "Draw" : "Pending";
    
};