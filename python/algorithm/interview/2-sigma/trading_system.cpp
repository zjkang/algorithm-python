#include <iostream>
using namespace std;
# include<map>

class TradingSystem {
private:
  map<float, int> sellMap; // increasing order
  map<float, int, greater<int>> buyMap; // decreasing order
  float totalProfit = 0.0;

public:
  int buy(int num_of_product, float price) {
    int totalBuy = 0;
    // for (auto it = sellMap.begin(); it != sellMap.end();) {
    //     float s_price = it->first;
    //     int s_count = it->second;
      for (auto [s_price, s_count] : sellMap) {
          if (price >= s_price) {
            int remain = num_of_product - s_count;
            if (remain < 0) {
              totalProfit += (price-s_price) * num_of_product;
              sellMap[s_price] = -remain;
              totalBuy += num_of_product;
              num_of_product = 0;
                
              // break;
            } else {
              totalProfit += (price-s_price) * s_count;
              num_of_product = remain;
              sellMap.erase(s_price);
              // it = sellMap.erase(it);
              totalBuy += s_count;
            }
          } else {
            break;
          }
    }

    if (num_of_product > 0) {
      buyMap[price] = num_of_product;
    }

    return totalBuy;
  }


  int sell(int num_of_product, float price) {
    int totalSell = 0;
    // for (auto it = buyMap.begin(); it != buyMap.end();) {
    //   float b_price = it->first;
    //   int b_count = it->second;
      for (auto [b_price, b_count] : buyMap) {
      if (price <= b_price) {
        int remain = num_of_product - b_count;
        if (remain < 0) {
          totalProfit += (b_price-price) * num_of_product;
          buyMap[b_price] = -remain;
          num_of_product = 0;
          totalSell += num_of_product;
            
          // break;
        } else {
          totalProfit += (b_price-price) * b_count;
          num_of_product = remain;
          buyMap.erase(b_price);
          // it = buyMap.erase(it);
          totalSell += b_count;
        }
      } else {
        break;
      }
    }

    if (num_of_product > 0) {
      sellMap[price] = num_of_product;
    }

    return totalSell;
  }

  float get_profits() {
    return totalProfit;
  }
};

// To execute C++, please define "int main()"
int main() {

  TradingSystem system;
  cout << system.sell(50, 1.5) << endl;
  cout << system.sell(20, 1.4) << endl;
  cout << system.buy(60, 1.51) << endl;
  cout << system.get_profits() << endl;
  cout << system.buy(20, 1.5) << endl;
  cout << system.get_profits() << endl;
  cout << system.sell(20, 0.7) << endl;
  cout << system.buy(100, 0.6) << endl;
  cout << system.get_profits()  << endl;

  return 0;
}


/*

Implement a trading system receiving incoming stream of trade orders. 

buy(num_of_product, price)
Called by buyer to buy certain number of products with a maximum price
num_of_product (INTEGER): number of products to buy
price (FLOAT): maximal price/unit the buyer is willing to pay
Return (INTEGER): number of products can be bought


sell(num_of_product, price)
Called by seller to sell certain number of products with a minimum price
num_of_product (INTEGER): number of products to sell
price (FLOAT): minimal price/unit the seller is willing to sell
Return (INTEGER): number of products can be sold


we take price difference between sell and buy orders as profits. We wanted to maximize the profits. 
get_profits()
Return (FLOAT): accumulated profits 


system = TradingSystem()
system.sell(50, 1.5)
return: 0

system.sell(20, 1.4)
return: 0

system.buy(60, 1.51) 
return: 60

system.get_profits() 
return: 2.6 60*1.51 - 20*1.4-40*1.5 = 2.6 

system.buy(20, 1.5)
return: 10              (10,1.5) (sell)

system.get_profits() 
return: 2.6.            

system.sell(20, 0.7)
return: 10         20*0.7=14.  (10 0.7)  

system.buy(100, 0.6)
return: 0.        0

system.get_profits() 
return: 10.6       2.6+(1.5-0.7)*10 = `10.6 
*/








