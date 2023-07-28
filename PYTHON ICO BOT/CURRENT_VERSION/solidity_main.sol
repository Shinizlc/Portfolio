// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
// import "hardhat/console.sol";
interface IUniswapV2Router {
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

contract Uniswap {

    address private constant uniswap_goerli = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;
    address private constant WETH = 0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6;
    address private immutable owner;

constructor() {
     owner = msg.sender;
}

modifier OnlyOwner() {
require(msg.sender == owner);
_;
}


    // function approve_token_to_Uniswap(address _token,uint _amount_to_send) OnlyOwner public{
    //     ERC20(_token).approve(uniswap_goerli,_amount_to_send);
    // }

    // function check_approval_for_contract() public OnlyOwner view OnlyOwner returns(uint) {
    //     return ERC20(WETH).allowance(address(this),uniswap_goerli);
    // }


    function _swap_token(address  _token_in, address  _token_out,uint _amountIn,uint _amountOutMin) external OnlyOwner {
        address[] memory path;
        ERC20(_token_in).approve(uniswap_goerli,_amountIn);
        if (_token_in==WETH || _token_out == WETH){
        path = new address[](2);
        path[0]=_token_in;
        path[1] = _token_out;}
        IUniswapV2Router(uniswap_goerli).swapExactTokensForTokensSupportingFeeOnTransferTokens(_amountIn, _amountOutMin, path, address(this), block.timestamp);
 }

    function getAmountOutMin(address _tokenIn, address _tokenOut, uint256 _amountIn) external view OnlyOwner returns (uint256) {

        address[] memory path;
        if (_tokenIn == WETH || _tokenOut == WETH) {
            path = new address[](2);
            path[0] = _tokenIn;
            path[1] = _tokenOut;}
        uint256[] memory amountOutMins = IUniswapV2Router(uniswap_goerli).getAmountsOut(_amountIn, path);
        return amountOutMins[path.length -1];}

///////CHECK pair contract liquidity
    function check_contract_liquidity(address pair_contract) public view OnlyOwner returns(uint weth_on_contract){
        return ERC20(WETH).balanceOf(pair_contract);
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


