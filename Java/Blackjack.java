import java.util.Random;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.Scanner;

public class Blackjack {
  Random random = new Random();
  /**
   * 1. トランプを2枚全プレイヤーに配ります。
   * 2. 子の数字が15以上の場合やめます。
   */
  ArrayList<Integer> list = new ArrayList<Integer>();
  Set<Integer> set = new HashSet<>(list);

  public int getNumber1_10() {
    int randomNumber = random.nextInt(12) + 1;
    if (randomNumber > 10) {
      randomNumber = 10;
    }
    return randomNumber;
  }

  public static void main(String args[]) {
    // 初期カード2枚のスコアを表示します。
    Random random = new Random();
    Scanner scanner = new Scanner(System.in);
    ArrayList<Integer> list = new ArrayList<>();
    list.add(1);
    list.add(1);

    Set<Integer> list_a = new HashSet<>();
    if (list.get(0) == 1 || list.get(1) == 1) {
      if (list.get(0) == 1) {
        list_a.add(1+list.get(1));
        list_a.add(11+list.get(1));
      }

      if (list.get(1) == 1) {
        list_a.add(list.get(0) + 1);
        list_a.add(list.get(0) + 11);
      }
    }
    System.out.println("2枚のカードの計算結果はこんな感じです。");
    for (Integer tmp : list_a) {
      System.out.println(tmp);
    }

    // カードを引くかを聞き、点数をあげるかどうかを決めます。
    while(true) {
      System.out.println("引きますか？ はい or いいえ");
      String yesOrNo = scanner.nextLine();
      if (yesOrNo.equals("はい")) {
        // はいの場合
        int nextRandomValue = random.nextInt(10) + 1;
        System.out.println(nextRandomValue + "を引きました。");
        Set<Integer> list_b = new HashSet<>();
        if (nextRandomValue == 1) {
          for (Integer tmp : list_a) {
            list_b.add(1 + tmp);
            list_b.add(11 + tmp);
          }
        } else {
          for (Integer tmp : list_a) {
            list_b.add(nextRandomValue + tmp);
          }
        }
    
        // 21より大きい場合、その値を削除します。
        list_b.removeIf(tmp -> tmp > 21);
    
        System.out.println("手札はこのようになってます。");
        for (Integer tmp : list_b) {
          System.out.println(tmp);
        }
        list_a = list_b;
        if (list_a.size() == 0) {
          System.out.println("あなたの負けです");
          break;
        }
      } else {
        // いいえの場合
        System.out.println("あたなの最終点数です。");
        for (Integer tmp : list_a) {
          System.out.println(tmp);
        }
        break;
      }
    }
  }
}
