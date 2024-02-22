# Header for DanhSach.txt
header = '{:<10}\t{:<20}\t{:<15}\t{}\n'.format("Ma ho", "Ten Ho", "Dia Diem", "KwPM")
with open("D:/CourseraWTF/FileParsing/DanhSach.txt", "a") as fi:
    fi.write(header)

with open("D:/CourseraWTF/FileParsing/DienNang.txt", "r") as ds:
    # Read lines until there are no more lines to read
    while True:
        Code = ds.readline().strip()  
        Name = ds.readline().strip()
        Location = ds.readline().strip()
        KwPM = ds.readline().strip()
        
        # Check if any of the variables are empty (indicating no more data)
        if not Code or not Name or not Location or not KwPM:
            break  # Exit the loop if any variable is empty
        
        # Format the data with appropriate width for each field
        formatted_data = '{:<10}\t{:<20}\t{:<15}\t{}\n'.format(Code, Name, Location, KwPM)
        
        # Append the formatted data to the "DanhSach.txt" file
        with open("D:/CourseraWTF/FileParsing/DanhSach.txt", "a") as fi:
            fi.write(formatted_data)
