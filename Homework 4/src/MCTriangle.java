import java.util.Random;

public class MCTriangle {
    static double sideLength = 0.5;
    static double radius = sideLength * 1/Math.sqrt(3);
    static double pi2 = 2*Math.PI;
    static double s60 = Math.sqrt(3)/2; //sin(pi/3) = .866, sin(2pi/3) = .866, sin(4pi/3) = -.866
    static double c60 = .5; //cos(pi/3) = 1/2, cos(2p/3) = -1/2, cos(4pi/3) = 1/2
    final static double Ay = radius;

    public static void main(String[] args){
        int crossed = 0;
        int tossed = 300000000;
        Random rnd = new Random();
        for (int i = 0; i < tossed; i++){
            double theta = rnd.nextDouble()*pi2;
            double center = rnd.nextDouble();
            double[] Ap = {Ay*Math.sin(theta), Ay*Math.cos(theta)};
            if (!(0 < Ap[1] + center && Ap[1] + center < 1)) //if A' crosses a line, increase counter, generate B'
            {
                crossed++;
            }
            else{
                double Byp = Ap[0]*s60 - Ap[1]*c60 + center;
                if (!(0 < Byp && Byp < 1)) //if B' crosses a line, increase counter, generate C'
                {
                    crossed++;
                }
                else{
                    double Cyp = -Ap[0]*s60 + Ap[1]*c60 + center;
                    if (!(0 < Cyp && Cyp < 1)) //if C' crosses a line, increase counter, else stop and iterate the loop
                    {
                        crossed++;
                    }
                }
            }
        }
        System.out.println("p = " + (double) crossed/tossed*100 + "%");
    }
}
