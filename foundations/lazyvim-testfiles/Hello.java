public class Hello {
  public static void main(String[] args) {
    System.out.println("Java Runner Test: SUCCESS");

    // Print passed arguments if any
    if (args.length > 0) {
      System.out.print("Arguments received: ");
      for (String arg : args) {
        System.out.print(arg + " ");
      }
      System.out.println();
    } else {
      System.out.println("No arguments passed.");
    }
  }
}
