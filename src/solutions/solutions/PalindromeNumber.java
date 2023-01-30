package solutions;

import static java.lang.String.valueOf;

public class PalindromeNumber {
    public static boolean isPalindrome(int x) {
        boolean result = false;
        if (x < 0) {
            result = false;
        } else {
            String num = Integer.toString(x);
            int length = num.length();
            for (int i = 0; i < length; i++) {
                if (num.charAt(i) == num.charAt(length - i - 1))
                    result = true;
            }
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println(isPalindrome(-10));
    }
}

