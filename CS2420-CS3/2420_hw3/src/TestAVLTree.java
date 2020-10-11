import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;
import java.util.Stack;

public class TestAVLTree {
    public static void main(String[] args) throws FileNotFoundException {
        AVLTree tree = new AVLTree();
        Scanner file = new Scanner(new FileReader("input.txt"));
        while(file.hasNext()){
            int num = file.nextInt();
            tree.insert(num);
        }
        tree.preorder();
    }
}
