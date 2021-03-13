#include <M5StickC.h>
const int initial_brightness = 10;

void setup(void)
{
    M5.begin();
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setRotation(1);
    M5.Axp.ScreenBreath(initial_brightness);
}

void loop(void)
{
    M5.Lcd.println("hello world");
    while(1){}
}
