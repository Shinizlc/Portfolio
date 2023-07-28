// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
// import "hardhat/console.sol";
interface IUniswapV2Router {
  function getAmountsOut(uint256 amountIn, address[] memory path)
    external
    view
    returns (uint256[] memory amounts);

  function swapExactTokensForTokens(

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
  ) external returns (uint256[] memory amounts);
}

contract Uniswap {

    address private constant uniswap_goerli = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;
    address private constant WETH_Goerli = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    //address private constant ETH_Goerli = 0x8d27431c473E83611847D195d325972e80D1F4c1;
    address private immutable owner;

constructor() {
     owner = msg.sender;
}


///call via web3
    function send_WETH_to_contract(uint _amount_to_send) public payable{
        ERC20(WETH_Goerli).transferFrom(msg.sender,address(this),_amount_to_send);
    }
    ////22.11.20220 swap token back adjustment
    // function approve_WETH_to_Uniswap(uint _amount_to_send) public{
    //     ERC20(WETH_Goerli).approve(uniswap_goerli,_amount_to_send);
    // }
        function approve_token_to_Uniswap(address _token,uint _amount_to_send) public{
        ERC20(_token).approve(uniswap_goerli,_amount_to_send);
    }

    function check_approval_for_contract() public view returns(uint) {
        return ERC20(WETH_Goerli).allowance(address(this),uniswap_goerli);
    }


    function _swap_token(address  _token_in,address  _token_out,uint _amountIn,uint _amountOutMin,address _to) external{
        address[] memory path;
        if (_token_in==WETH_Goerli || _token_out == WETH_Goerli){
        path = new address[](2);
        path[0]=_token_in;
        path[1] = _token_out;}
        else {
            path = new address[](3);
            path[0] = _token_in;
            path[1] = WETH_Goerli;
            path[2] = _token_out;
        }
        IUniswapV2Router(uniswap_goerli).swapExactTokensForTokens(_amountIn, _amountOutMin, path, _to, block.timestamp);
 }

       function getAmountOutMin(address _tokenIn, address _tokenOut, uint256 _amountIn) external view returns (uint256) {

        address[] memory path;
        if (_tokenIn == WETH_Goerli || _tokenOut == WETH_Goerli) {
            path = new address[](2);
            path[0] = _tokenIn;
            path[1] = _tokenOut;
        } else {
            path = new address[](3);
            path[0] = _tokenIn;
            path[1] = WETH_Goerli;
            path[2] = _tokenOut;
        }

        uint256[] memory amountOutMins = IUniswapV2Router(uniswap_goerli).getAmountsOut(_amountIn, path);
        return amountOutMins[path.length -1];}

///////////////////////////////////////////////////////////////////CHECK pair contract liquidity
    function check_contract_liquidity(address pair_contract) public view returns(uint weth_on_contract){
        return ERC20(WETH_Goerli).balanceOf(pair_contract);
    }

 //////////////////////////////////////////////////////////////////
    // function get_balance_ETH() public view returns(uint) {
    //     return address(this).balance;
    // }
/////////22.11.20220 swap token back adjustment
    // function get_balance_WETH() public view returns(uint){
    //     return ERC20(WETH_Goerli).balanceOf(address(this));
    // }

    function get_balance_token(address _token) public view returns(uint){
        return ERC20(_token).balanceOf(address(this));
    }

    function get_token_decimals(address _token) public view returns(uint){
        return ERC20(_token).decimals();
    }
///we may also transfer all balance:
/// balance = get_balance_token()
//ERC20(WETH_Goerli).transfer(msg.sender,balance);

    function send_weth_to_wallet(uint _amount) public{
        ERC20(WETH_Goerli).transfer(owner,_amount);
    }

    function withdraw_funds() public {
        (bool success_flag,) = payable(owner).call{value:address(this).balance}("");
        require(success_flag,'The withdraw was unsuccefull');
    }

        fallback() external payable{}
        receive() external payable{}

}
