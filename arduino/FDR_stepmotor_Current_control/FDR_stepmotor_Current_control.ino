#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include <WProgram.h>
#endif
#include <ros.h>
#include <std_msgs/MultiArrayLayout.h>
#include <std_msgs/MultiArrayDimension.h>
#include <std_msgs/UInt16MultiArray.h>
#include <std_msgs/Float64MultiArray.h>
#include <Arduino.h>
#include "BasicStepperDriver.h"
#include "MultiDriver.h"
#include "SyncDriver.h"
#define MOTOR_STEPS 200
#define MOTOR_X_RPM 50
#define MOTOR_Y_RPM 50
#define DIR_X 4
#define STEP_X 3
#define DIR_Y 7
#define STEP_Y 6
#define MICROSTEPS1 32
#define MICROSTEPS2 32
BasicStepperDriver stepperX(MOTOR_STEPS, DIR_X, STEP_X);
BasicStepperDriver stepperY(MOTOR_STEPS, DIR_Y, STEP_Y);
SyncDriver controller(stepperX, stepperY);
int en1a = 8 , en1b = 9, pwm_L = 10, pwm_R = 11, x = 0, val = 0, degree1, degree2,previous_angle1 = 0, previous_angle2 = 0; //R1_pwm
float  Kp = 20,  val_pre = 0, Samples = 0.0, control = 0, current= 0,AvgAcs=0,error=0,des_current=0,total_error=0,pre_error=0;
float sensorValue = 0;
float mVperAmp = 0.31; // 185 5A MODÜL İÇİN , 100 20A MODÜL İÇİN VE 66  30A MODÜL İÇİN
double Amps = 0;// AMPER HESABI
float ACSoffset = 2.5;
float step_m=1;
ros::NodeHandle nh;
void data( const std_msgs::Float64MultiArray& cmd_msg) {
  des_current = cmd_msg.data[0] ;
  degree1 = cmd_msg.data[1];
  degree2 = cmd_msg.data[2];
  control = cmd_msg.data[3];
}
ros::Subscriber<std_msgs::Float64MultiArray> sub("step", data);
void setup() {
  nh.initNode();
  nh.subscribe(sub);
  stepperX.begin(MOTOR_X_RPM, MICROSTEPS1);
  stepperY.begin(MOTOR_Y_RPM, MICROSTEPS2);
  pinMode(pwm_L, OUTPUT);  //Tüm pinlerden güç çıkışı olacağı için OUTPUT olarak ayarladık.
  pinMode(pwm_R, OUTPUT);
  pinMode(en1a, OUTPUT);
  pinMode(en1b, OUTPUT);
}
void loop() {

  if (previous_angle1*step_m != degree1*step_m || previous_angle2*step_m != degree2 *step_m )
  {
    controller.rotate(int(degree1*step_m  - previous_angle1*step_m), int(degree2*step_m - previous_angle2*step_m));
  }
  previous_angle1 = degree1;
  previous_angle2 = degree2;
  controller.rotate(0, 0);
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  digitalWrite(en1a, HIGH);
  digitalWrite(en1b,  HIGH);
  analogWrite(pwm_R,  0);
  
  if (des_current != 0) {
    analogWrite(pwm_L,  val);
  }
  if (des_current == 0) {
    analogWrite(pwm_L,  0);
  }
  float AcsValue = 0.0, Samples = 0.0, AvgAcs = 0.0, AcsValueF = 0.0;
  //float AcsValue2 = 0.0, Samples2 = 0.0, AvgAcs2 = 0.0, AcsValueF2 = 0.0;
  for (int x = 0; x < 200; x++) { //Get 150 samples
    AcsValue = analogRead(A5);     //Read current sensor values
    Samples = Samples + AcsValue;  //Add samples together
    delay (1); // let ADC settle before next sample 3ms
  }
  AvgAcs = Samples / 200.0; //Taking Average of Samples
  Amps = ((-ACSoffset + ((AvgAcs / 1024.0) * 5.0) ) / (mVperAmp)); // AKIM HESAPLA
  current =  2.5  * Amps - 0.14;
  
  error = des_current - current;
  total_error=total_error+error;
  val = (error * 30) +total_error*3+(error-pre_error)*0.05+val_pre*0.9;
  val = constrain(val, 0, 250);
  val_pre = val;
  pre_error=error;
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  nh.spinOnce();
  delay(1);
}
