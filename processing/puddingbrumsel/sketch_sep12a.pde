import rita.*;

RiText rts;
RiGrammar grammar;

void setup() 
{
  size(650, 200);
  RiText.setDefaultAlignment(CENTER);
  RiText.setDefaultFont("FetteEgyptienne24.vlw");
  rts = new RiText(this, "pudding?", width/2, height/2-12);
  grammar = new RiGrammar(this, "pudding.g");
}

void draw()
{
  background(255);

  String result = grammar.expand();
  rts.fadeToText(result, 1.0f);
  delay(1000);
}  

