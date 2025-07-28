class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        int[] answer = new int[s.length()];
        for(int i = 0; i < s.length(); i++){
            answer[i] = Integer.parseInt(s.substring(answer.length-1-i, answer.length-i));
        }
        return answer;
    }
}
/*
1. n을 String으로 바꾼다
2. n의 길이만큼 반복문을 돌면서 배열에 저장한다
3. 배열을 return한다
*/