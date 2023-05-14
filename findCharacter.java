import java.util.*;
class Main{
    public int solution(String str, char t){
        int answer = 0;
        str=str.toUpperCase(); //string을 다 대문자화
        t=Character.toUpperCase(t); 
        //System.out.println(str+""+t);
        // for(int i=0; i<str.length(); i++){
        //     if(str.charAt(i)==t) answer++;

        //     }

        for(char x : str.toCharArray()){ //toCharArray: 스트링에 있는 문자 하나하나를 분리해서 문자를 원소로 하는 문자 배열을 만들어야 함
            if(x==t) answer++;
        }
            return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next(); //문자열 하나 읽어들이기
        char c = kb.next().charAt(0); //string을 index로 받아들인다는 뜻. 0번째를 가져와라
        System.out.print(T.solution(str, c));

    }
}