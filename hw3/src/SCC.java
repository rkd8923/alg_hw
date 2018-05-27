import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;

public class SCC {
	static int N = 0;
	static AdjacencyMatrix MATRIX;
    static AdjacencyList LIST;
	public static void main(String args[]) {
		// Input setting
        try {
			BufferedReader input = new BufferedReader(new FileReader(args[0]));
			int i = 0;
			String s;

			while ((s = input.readLine()) != null) {
				s = s.trim();
                if (i == 0) {
                    N = Integer.parseInt(s);
                    MATRIX = new AdjacencyMatrix(N);
                    LIST = new AdjacencyList(N);
                }
                else setInput(i, s);
                i++;
			}
			input.close();
		}
    	catch (IOException e) {
    		System.err.println(e); 
    		System.exit(1);
    	}

        // Strongly Connected Component
        ArrayList<Integer>[] scc_matrix = MATRIX.scc();
		print_scc(scc_matrix);
	}
    public static void setInput(int i, String s) { 
    	String[] str_nums = s.split("\\s");
    	int[] nums = Arrays.stream(str_nums).mapToInt(Integer::parseInt).toArray();
    	MATRIX.setInput(i, nums);
    	LIST.setInput(i, nums);
    }
    public static void print() {
    	for (int x = 1; x <4; x++) {
    		for (int y=1; y<4; y++)
    			System.out.print(MATRIX.getElement(x, y) + " ");
    		System.out.print("\n");
    	}
    }
    public static void transprint() {
       	for (int x = 1; x <4; x++) {
       		for (int y=1; y<4; y++)
       			System.out.print(MATRIX.getTrans(x, y) + " ");
       		System.out.print("\n");
       	}
    }
    public static void print_scc(ArrayList<Integer>[] m) { 
    	for (int i=1; i<m.length; i++) {
    		if (m[i] == null) continue;
    		for (int j=0; j<m[i].size(); j++)
    			System.out.print(m[i].get(j)+ " ");
    		System.out.print("\n");
    	}
    }
}
