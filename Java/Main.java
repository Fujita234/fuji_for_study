import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Player player1 = new Player();
    Player player2 = new Player();

    Scanner scanner = new Scanner(System.in);
    int ans = 0;
    while(true) {
      System.out.println("0~9の中の値を入力してください");
      ans = scanner.nextInt();
      if (0 <= ans && ans < 10) {
        break;
      } else {
        System.out.println("日本語読め");
      }
    }
  }
}