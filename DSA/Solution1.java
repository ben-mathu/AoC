import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution1 {
  public static int count(String text) {
    int count = 0;

    String formattedText = text;
    Pattern pattern = Pattern.compile("/[ ]+?\\*.*\\*/");
    for (int i = 0; ; i++) {
      Matcher matcher = pattern.matcher(formattedText);
      if (matcher.find()) {
        formattedText = formattedText.replaceAll("/[ ]+?\\*.*\\*/", "");
      } else break;
    }

    System.out.println(formattedText);

    // String[] source = text.split("\n");

    // int count = 0;
    // for (int i = 0; i < source.length; i++) {

    // }
    // System.out.println(count);

    return count;
  }

  public static void main(String[] args) {
    count(
        "/** 1. This is a single line multiline comment */\n" +
        "/** 2.\n" + 
        "* This is a simple program to print hello world\n" +
        "*/\n"+
        "/*******//* 3.\n" + 
        " This is a simple program to print hello world\n" +
        "*/\n"
        + "public class Example2 {\n" +
        "\tpublic static void main(String[] args) {\n" +
        "\n" +
            "\t\t// 4. say hello\n" +
            "\t\tSystem.out.println(\"Hello world!\");\n" +
        "\t}\n" +
    "}");
  }
}