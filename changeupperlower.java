import java.util.*;

class Main{
    public String solution(String str){
        String answer = "";
        for(char x: str.toCharArray()){
            if(Character.isLowerCase(x)) answer+=Character.toUpperCase(x);
            else answer+=Character.toLowerCase(x);
        } //transform from string to character array
        return answer;
    }


public static void main(String[] args) {
    Main T = new Main();
    Scanner kb = new Scanner(System.in);
    String str = kb.next();
    System.out.println(T.solution(str));
    }  
}