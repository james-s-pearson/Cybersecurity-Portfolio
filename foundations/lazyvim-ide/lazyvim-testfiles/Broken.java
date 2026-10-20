// Deliberately broken: the missing semicolon below is the point.
// F5 should show a compiler error and run nothing.
public class Broken {
  public static void main(String[] args) {
    System.out.println("This line never runs")
  }
}
