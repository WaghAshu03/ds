import java.io.*;

public class Weather {
    public static void main(String[] args) throws IOException {
        String filePath="D:\\Academics\\3rd Year\\Sem 6\\Practicals\\DSBDAL\\15 . Locate dataset (e.g Sample_weather.txt) for working on weather data\\simple.txt";

        BufferedReader reader=new BufferedReader(new FileReader(filePath));

        //Skip the header line
        String line=reader.readLine();

        //Initialize the sum and count variable
        double sumTemp=0;
        double sumDewPoint=0;
        double sumWindSpeed=0;
        int count=0;

        //read each line of file
        while((line= reader.readLine())!=null){
            //split line into field
            String[] fields=line.split(",");

            //Parse values
            double temp=Double.parseDouble(fields[1]);
            double dewPoint=Double.parseDouble(fields[2]);
            double windSpeed=Double.parseDouble(fields[3]);

            //add value to sum variable
            sumTemp+=temp;
            sumDewPoint+=dewPoint;
            sumWindSpeed+=windSpeed;

            //increment counter
            count++;
        }
        //calculate average
        double avgTemp=sumTemp/count;
        double avgDewPoint=sumDewPoint/count;
        double avgWindSpeed=sumWindSpeed/count;

        //Print average
        System.out.println("Avg Temp "+avgTemp);
        System.out.println("Avg Dew Point "+avgDewPoint);
        System.out.println("Avg wind Speed "+avgWindSpeed);

        //close reader
        reader.close();
    }
}
