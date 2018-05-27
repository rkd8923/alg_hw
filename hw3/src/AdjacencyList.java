import java.util.ArrayList;

public class AdjacencyList {
	ArrayList<ArrayList<Integer>> list = new ArrayList<>();
	ArrayList<Integer> dummy = new ArrayList<>();
	
	public AdjacencyList(int n) {
		this.list.add(this.dummy);
		for (int i = 1; i <= n; i++) { 
			ArrayList<Integer> tmp = new ArrayList<>();
			tmp.add(0);
			this.list.add(tmp);
		}
	}
	public void setInput(int n, int[] input) {
		for (int i=0; i<input.length; i++)
			if (input[i] != 0) this.list.get(n).add(input[i]);
	}
	public ArrayList<Integer> getLine(int x) {
		return this.list.get(x);
	}
}
