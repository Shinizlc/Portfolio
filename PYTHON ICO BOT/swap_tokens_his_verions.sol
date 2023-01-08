function swapToken(address tokenIn, address tokenOut, uint amountIn, uint amountOutMin, address to) external {
// Define the path of tokens to swap through
address[] memory path;
if (tokenIn == WETH_Goerli || tokenOut == WETH_Goerli) {
path = new address[](2);
path[0] = tokenIn;
path[1] = tokenOut;
} else {
path = new address[](3);
path[0] = tokenIn;
path[1] = WETH_Goerli;
path[2] = tokenOut;
}

// Perform the token swap
IUniswapV2Router(uniswap_goerli).swapExactTokensForTokens(amountIn, amountOutMin, path, to, block.timestamp);
}

function getAmountOutMin(address tokenIn, address tokenOut, uint amountIn) external view returns (uint) {
// Define the path of tokens to swap through
address[] memory path;
if (tokenIn == WETH_Goerli || tokenOut == WETH_Goerli) {
path = new address[](2);
path[0] = tokenIn;
path[1] = tokenOut;
} else {
path = new address[](3);
path[0] = tokenIn;
path[1] = WETH_Goerli;
path[2] = tokenOut;
}

// Get the minimum amount of the output token that can be received
uint[] memory amountOutMins = IUniswapV2Router(uniswap_goerli).getAmountsOut(amountIn, path);
return amountOutMins[path.length - 1];
}

function getTokenBalance(address token) public view returns (uint) {
// Get the balance of the specified token for the contract
return ERC20(token).balanceOf(address(this));
}