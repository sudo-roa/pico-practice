# num-counter
数字を数える

## 概要
LED及びLCD1602をつかって数字を表示<br>
現段階ではcountupのみ

## 配線
LCD1602 -> pico
- GND -> GND
- VCC -> 
- SDA -> 
- SCL -> 

LED(4つ) -> pico
- (-) -> GND
- (+) -> GPIO(16,17,18,19)
    - 0bit目のLED -> 16
    - 1bit目のLED -> 17
    - 2bit目のLED -> 18
    - 3bit目のLED -> 19

### ライブラリ
- lcd1602.py

## 参考
[SunFounder](https://www.sunfounder.com)
