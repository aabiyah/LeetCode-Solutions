package solutions;

public class RomanToInteger {
    public Integer romanToInt(String s) {
        if(s == null){
            return 0;
        }

        int length = s.length();
        int total = 0;
        int before = 0;

        for(int i = length - 1; i >= 0; i--){
            int current = romanTable(s.charAt(i));

            if(i == length - 1){
                total += current;
            }else{
                if(current < before){
                    total -= current;
                }else{
                    total += current;
                }
            }
            before = current;
        }

        return total;
    }

    public int romanTable(char c){
        int num = 0;
        switch(c){
            case 'I':
                num = 1;
                break;
            case 'V':
                num = 5;
                break;
            case 'X':
                num = 10;
                break;
            case 'L':
                num = 50;
                break;
            case 'C':
                num = 100;
                break;
            case 'D':
                num = 500;
                break;
            case 'M':
                num = 1000;
                break;
            default:
                num = 0;
                break;
        }
        return num;
    }
    public static void main(String[] args) {
        RomanToInteger ob1 = new RomanToInteger();
        System.out.printf(String.valueOf(ob1.romanToInt("XV")));
    }
}

