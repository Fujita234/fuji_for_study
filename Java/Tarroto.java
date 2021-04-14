/**
 * Tarrot君はAの世界にいる。
 * Scanner君はBの世界にいる。
 * ということを前提に話が進みます。
 */

// Aの世界からBの世界へ転生してきた
import java.util.Scanner;  // importはBの世界にいるScanner君を呼んでいる
import java.util.Random; // importはCの世界にいるRandom君を呼んでいる

public class Tarroto {
  public static void main(String args[]) {
    System.out.println("お名前なんていうですか？");
    Scanner scanner = new Scanner(System.in);
    Random random = new Random();

    String str = scanner.next();
    System.out.println(str);

    int randomValue = random.nextInt(42);
    System.out.println(randomValue);

    // double divValue = randomValue / 2;
    double divValue = 10.5;
    System.out.println((int)divValue);
  }
}