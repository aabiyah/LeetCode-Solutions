package solutions;

import static java.lang.String.valueOf;

public class PalindromeNumber {
    public static boolean isPalindrome(int x) {
        boolean result = true;
        String str = Integer.toString(x);
        int length = str.length();
        for (int i = 0; i <= (length / 2) - 1; i++) {
            if (str.charAt(i) != str.charAt(length - i - 1)) {
                result = false;
                break;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(100));
    }
}

