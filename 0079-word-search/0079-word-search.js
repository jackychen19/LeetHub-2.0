/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length,
          cols = board[0].length;
    
    let path = new Set();
    
    const dfs = (r, c, i) => {
        if (i === word.length) return true;
        
        const coords = `${r} ${c}`;
        if (path.has(coords)
           || r < 0 || c < 0 || r === rows || c === cols
           || board[r][c] !== word[i]) return false;
        
        path.add(coords);
        let result = (dfs(r + 1, c, i + 1)
                    || dfs(r - 1, c, i + 1)
                    || dfs(r, c + 1, i + 1)
                    || dfs(r, c - 1, i + 1))
        path.delete(coords);
        return result;
    }
    
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (dfs(r, c, 0)) return true;
        }
    }
    
    return false;
};