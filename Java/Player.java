import java.util.Random;
import java.util.ArrayList;

public class Player {
  
  public int[] decideNumbers(int answer) {
    //1～10の整数値を持つリストを用意
    ArrayList<Integer> list = new ArrayList<Integer>();
    for(int i = 0 ; i <= 10 ; i++) {
      list.add(i);
    }
  
    int[] selectedNumber = new int[answer];
    Random random = new Random();
    for (int i = 0; i < answer; i++) {
      selectedNumber[i] = list.get(random.nextInt(10-i));
      list.remove(i);
    }
    return selectedNumber;
  }
}