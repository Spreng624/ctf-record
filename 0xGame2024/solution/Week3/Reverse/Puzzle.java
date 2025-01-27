import java.util.Scanner;

public class Puzzle {
   static int[][] board = new int[][] {
         { 5, 7, 0, 9, 4, 0, 8, 0, 0 },
         { 0, 0, 8, 0, 3, 0, 0, 0, 5 },
         { 0, 1, 0, 2, 0, 0, 0, 3, 7 },
         { 0, 0, 9, 7, 2, 0, 0, 0, 0 },
         { 7, 3, 4, 0, 0, 8, 0, 0, 0 },
         { 0, 0, 0, 0, 0, 0, 7, 5, 1 },
         { 3, 0, 0, 0, 1, 4, 2, 0, 0 },
         { 0, 6, 0, 0, 0, 2, 0, 4, 0 },
         { 0, 2, 7, 0, 0, 9, 5, 0, 0 } };

   public static void exit() {
      System.out.println("解谜失败");
      System.exit(1);
   }

   public static boolean check(int x, int y) {
      int t = board[x][y];
      int x_ = x - x % 3;
      int y_ = y - y % 3;

      int i;
      for (i = 0; i < 9; ++i) {
         if (i != x && i != y && (t == board[x][i] || t == board[i][y])) {
            return false;
         }
      }

      for (i = 0; i < 3; ++i) {
         for (int var6 = 0; var6 < 3; ++var6) {
            if (x_ + i != x && y_ + var6 != y && t == board[x_ + i][y_ + var6]) {
               return false;
            }
         }
      }

      return true;
   }

   static String flag(String answer) {
      StringBuilder s = new StringBuilder();

      for (int i = 0; i < answer.length(); i += 6) {
         int var3 = Integer.parseInt(answer.substring(i, i + 6));
         s.append(Integer.toHexString(var3));
      }

      return s.toString();
   }

   public static void main(String[] var0) {
      System.out.println("请输入你的解谜结果:");
      Scanner scanner = new Scanner(System.in);
      String answer = scanner.nextLine();
      scanner.close();
      if (answer.length() != 48) {
         exit();
      }

      int var3 = 0;

      int i;
      int j;
      for (i = 0; i < 9; ++i) {
         for (j = 0; j < 9; ++j) {
            if (board[i][j] == 0) {
               int var6 = answer.charAt(var3) - 48;
               if (var6 > 0 && var6 <= 9) {
                  board[i][j] = var6;
                  ++var3;
               } else {
                  exit();
               }
            }
         }
      }

      for (i = 0; i < 9; ++i) {
         for (j = 0; j < 9; ++j) {
            if (!check(i, j)) {
               exit();
            }
         }
      }

      System.out.println(String.format("0xGame{%s}", flag(answer)));
   }
}
