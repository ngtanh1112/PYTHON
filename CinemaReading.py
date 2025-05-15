import csv
from collections import defaultdict


def read_cinema_from_file(fileName):
    """
    Hàm đọc file dữ liệu về rạp chiếu phim. Hàm này thực hiện việc đọc dữ liệu
    các rạp chiếu phim từ tệp có tên fileName có định dạng csv.
    Sau đó, tạo ra các từ điển Cinema tương ứng và lưu vào một danh sách.
    """
    cinemas = []

    with open(fileName, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            cinema = {
                'name': row['name'],
                'cid': row['cid'],
                'investor': row['investor']
            }
            cinemas.append(cinema)

    return cinemas


def count_investor(cinema_list):
    """
    Hàm tính và trả về một từ điển số lượng cinema tương ứng với mỗi investor.
    """
    investor_count = defaultdict(int)

    for cinema in cinema_list:
        investor_count[cinema['investor']] += 1

    return dict(investor_count)


def read_cinema_movies_from_file(fileName, cinema_list):
    """
    Hàm đọc file số vé bán ra mỗi bộ phim được chiếu bởi mỗi rạp
    để bổ sung thêm thông tin cho cinema_list.
    """
    with open(fileName, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        # Duyệt từng dòng trong file csv
        for row in csv_reader:
            # Lấy cid của rạp từ file
            cid = row['cid']

            # Tìm rạp trong cinema_list theo cid
            for cinema in cinema_list:
                if cinema['cid'] == cid:
                    # Thêm thông tin về số vé bán cho các bộ phim
                    cinema['movies'] = {movie: int(row[movie]) for movie in row if movie != 'cid'}
                    break

    return cinema_list


def get_max_cinema(cinema_list):
    """
    Hàm thực hiện việc tính và trả về cid của cinema có tổng số vé bán ra là lớn nhất.
    cid đầu tiên có giá trị max (nếu có nhiều hơn 1 cid cùng giá số vé lớn nhất)
    """
    max_cinema = None
    max_sales = 0

    for cinema in cinema_list:
        total_sales = sum(cinema['movies'].values()) if 'movies' in cinema else 0

        if total_sales > max_sales:
            max_sales = total_sales
            max_cinema = cinema['cid']

    return max_cinema
