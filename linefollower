//definição dos pinos
#define ldrE A0
#define ldrD A1
#define ledE 13
#define ledD 2
#define motorE 11
#define motorD 10

//variáveis referentes ao valor do ldr
int valorldrE;
int valorldrD;

void setup(){
  //definição das saídas
  pinMode(ledE, OUTPUT);
  pinMode(ledD, OUTPUT);
  pinMode(motorE, OUTPUT);
  pinMode(motorD, OUTPUT);
  Serial.begin(9600);
  
  //Leds permanecem ligados para leitura do ldr de acordo com a luminosidade refletida
  digitalWrite(ledE, HIGH);
  digitalWrite(ledD, HIGH);
}

void loop(){
  valorldrE = analogRead(ldrE);
  valorldrD = analogRead(ldrD);
  Serial.println(valorldrE);
  Serial.println(valorldrD);
  //Ir para frente 
  if(valorldrE<345 && valorldrD<345){
    Frente(255);
  }
  
  //Virar para a Esquerda
  if(valorldrE<345 && valorldrD>345){
    Esquerda(255);
  }
  
  //Virar para a Direita
  if(valorldrE>345 && valorldrD<345){
    Direita(255);
  }
  
  //Freiar
  if(valorldrE>345 && valorldrD>345){
    Freiar(0);
  }
}
//Função para ligar os dois motores
void Frente(int valor){
  analogWrite(motorE, valor);
  analogWrite(motorD, valor);
}

//Função para ligar apenas o motor da esquerda
void Esquerda(int valor){
  analogWrite(motorE, valor);
  analogWrite(motorD, 0);
}

//Função para ligar apenas o motor da direita
void Direita(int valor){
  analogWrite(motorE, 0);
  analogWrite(motorD, valor);
}

//Função para desligar os motores
void Freiar(int valor){
  analogWrite(motorE, valor);
  analogWrite(motorD, valor);
}
