class Solution {
    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder("");
        int temp = num;

        int divider = 1000;
        while (divider > 0){
            int quot = temp / divider;
            temp = temp % divider;

            if (quot == 0){
                divider = divider/10;
                continue;
            }

            sb.append(getString(quot, divider));
            divider /= 10;
        }

        return sb.toString();
    }

    private String getString(int quot, int divider){
        String digit_1 = "", digit_5 = "", digit_10 = "";
        switch (divider){
            case 1:
                digit_1 = "I";
                digit_5 = "V";
                digit_10 = "X";
                break;
            case 10:
                digit_1 = "X";
                digit_5 = "L";
                digit_10 = "C";
                break;

            case 100:
                digit_1 = "C";
                digit_5 = "D";
                digit_10 = "M";
                break;

            case 1000:
                digit_1 = "M";
                break;
            }
        String roman = "";
        switch (quot){
            case 4:
                roman += digit_1 + digit_5;
                break;
            case 5:
                roman += digit_5;
                break;
            case 9:
                roman += digit_1 + digit_10;
                break;
            default:
                if(quot < 5){
                    for (int i = 0; i < quot; i++){
                        roman += digit_1;
                    }
                } else if (quot < 9){
                    roman += digit_5;
                    for (int i = 0; i < quot-5; i++){
                        roman += digit_1;
                    }   
                }
        }
        return roman;
    }
}