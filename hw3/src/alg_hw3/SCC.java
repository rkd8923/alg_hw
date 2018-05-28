package alg_hw3;
import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;

public class SCC {
	static int N = 0;
	static AdjacencyMatrix MATRIX;
    static AdjacencyList LIST;
    static AdjacencyArray ARRAY;
    static long[] times = new long[3];
    
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
                    ARRAY = new AdjacencyArray(N);
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

        // Adjacency Matrix
    	long start = System.currentTimeMillis();
        ArrayList<Integer>[] scc_matrix = MATRIX.scc();    	
    	long end = System.currentTimeMillis();
    	times[0] = end - start;
    	
    	// Adjacency List
    	start = System.currentTimeMillis();
        ArrayList<Integer>[] scc_list = LIST.scc();    	
    	end = System.currentTimeMillis();
    	times[1] = end - start;
    	
    	// Adjacency Array
   	    start = System.currentTimeMillis();
        ArrayList<Integer>[] scc_array = ARRAY.scc();    	
       	end = System.currentTimeMillis();
        times[2] = end - start;
	    
	    print_scc(scc_matrix);
		System.out.println("Adjacency Matrix time : " + times[0]);
		print_scc(scc_list);
		System.out.println("Adjacency List time : " + times[1]);
		print_scc(scc_array);
		System.out.println("Adjacency Array time : " + times[2]);
	}
    public static void setInput(int i, String s) { 
    	String[] str_nums = s.split("\\s");
    	int[] nums = Arrays.stream(str_nums).mapToInt(Integer::parseInt).toArray();
    	MATRIX.setInput(i, nums);
    	LIST.setInput(i, nums);
    	ARRAY.setInput(i, nums);
    }

//    public static void print() {
//    	for (int x = 1; x <4; x++) {
//    		for (int y=1; y<4; y++)
//    			System.out.print(MATRIX.getElement(x, y) + " ");
//    		System.out.print("\n");
//    	}
//    }
//    public static void transprint() {
//       	for (int x = 1; x <4; x++) {
//       		for (int y=1; y<4; y++)
//       			System.out.print(MATRIX.getTrans(x, y) + " ");
//       		System.out.print("\n");
//       	}
//    }
    public static void print_scc(ArrayList<Integer>[] m) { 
    	for (int i=1; i<m.length; i++) {
    		if (m[i] == null) continue;
    		for (int j=0; j<m[i].size(); j++)
    			System.out.print(m[i].get(j)+ " ");
    		System.out.print("\n");
    	}
    }
}
