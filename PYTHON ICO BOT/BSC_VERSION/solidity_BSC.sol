// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

interface IPanecakeswap {
  function getAmountsOut(uint256 amountIn, address[] memory path)
    external
    view
    returns (uint256[] memory amounts);

  function swapExactTokensForTokensSupportingFeeOnTransferTokens(

    //amount of tokens we are sending in
    uint256 amountIn,
    //the minimum amount of tokens we want out of the trade
    uint256 amountOutMin,
    //list of token addresses we are going to trade in.  this is necessary to calculate amounts
    address[] calldata path,
    //this is the address we are going to send the output tokens to
    address to,
    //the last time that the trade is valid for
    uint256 deadline
  ) external;
}

contract Pancakeswap {

    address private constant cake_router = 0x10ED43C718714eb63d5aA57B78B54704E256024E;
    address private constant WBNB = 0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c;
    address private immutable owner;

constructor() {
     owner = msg.sender;
}

modifier OnlyOwner() {
require(msg.sender == owner);
_;
}



function buy(address _tokenIn, address _tokenOut, uint256 _amountIn, uint256 _amountOutMin) public OnlyOwner {
      
    ERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);
    
    ERC20(_tokenIn).approve(cake_router, _amountIn);
  
    address[] memory path = new address[](2);
    path[0] = _tokenIn;
    path[1] = _tokenOut;

    IPanecakeswap(cake_router).swapExactTokensForTokensSupportingFeeOnTransferTokens(_amountIn, _amountOutMin, path, address(this), block.timestamp);
    }


    
   function sell(address _tokenIn, address _tokenOut, uint256 _amountIn, uint256 _amountOutMin) public OnlyOwner {

    ERC20(_tokenIn).approve(cake_router, _amountIn);

   
    address[] memory path = new address[](2);
    path[0] = _tokenIn;
    path[1] = _tokenOut;

        IPanecakeswap(cake_router).swapExactTokensForTokensSupportingFeeOnTransferTokens(_amountIn, _amountOutMin, path, owner, block.timestamp);
    }


    function getAmountOutMin(address _tokenIn, address _tokenOut, uint256 _amountIn) external view OnlyOwner returns (uint256) {

        address[] memory path;
        if (_tokenIn == WBNB || _tokenOut == WBNB) {
            path = new address[](2);
            path[0] = _tokenIn;
            path[1] = _tokenOut;}
        uint256[] memory amountOutMins = IPanecakeswap(cake_router).getAmountsOut(_amountIn, path);
        return amountOutMins[path.length -1];}

///////CHECK pair contract liquidity
    function check_contract_liquidity(address pair_contract) public view OnlyOwner returns(uint weth_on_contract){
        return ERC20(WBNB).balanceOf(pair_contract);
    }


    function get_balance_token(address _token) public view OnlyOwner returns(uint){
        return ERC20(_token).balanceOf(address(this));
    }

    function get_token_decimals(address _token) public view OnlyOwner returns(uint){
        return ERC20(_token).decimals();
    }

    function send_token_to_wallet(uint _amount, address token) public OnlyOwner {
        ERC20(token).transfer(owner,_amount);
    }

    function withdraw_funds() public OnlyOwner{
        (bool success_flag,) = payable(owner).call{value:address(this).balance}("");
        require(success_flag,'The withdraw was unsuccefull');
    }

        fallback() external payable{}
        receive() external payable{}

}


