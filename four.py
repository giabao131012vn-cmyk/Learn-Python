task = []
is_editing = True

while is_editing == True:
    print('MENU: ')
    print("1. Thêm công việc")
    print("2. Xem danh sách công việc")
    print('3. Xóa công việc đã xong')
    print('4. Thoát')

    while True:

        try:
            selected_menu = int(input('Hãy chọn một chế độ bằng số thứ tự của nó: '))

            if selected_menu == 1:
                add_task_name = input('Hãy thêm một công việc vào danh sách: ')
                add_task_status = input('Công việc đó đã xong chưa (Chưa xong/Đã xong): ')

                while add_task_status.lower() != "chưa xong" and add_task_status.lower() != "đã xong":
                    print('Câu trả lời không hợp lệ')
                    add_task_status = input('Công việc đó đã xong chưa (Chưa xong/Đã xong): ')

                if add_task_status.lower() == "chưa xong":
                    task.append({"Tên công việc": add_task_name, "Trạng thái": "Chưa hoàn thành"})
                    print('Đã thêm một công việc mới vào danh sách')
                
                elif add_task_status.lower() == "đã xong":
                    task.append({"Tên công việc": add_task_name, "Trạng thái": "Đã hoàn thành"})
                    print('Đã thêm một công việc mới vào danh sách')

            elif selected_menu == 2:
                if len(task) != 0:
                    print("Đây là danh sách chứa toàn bộ công việc của bạn: ")
                    for jobs in task:
                        print(f'{jobs["Tên công việc"]}: {jobs["Trạng thái"]}')
                else:
                    print("Danh sách của bạn trống rỗng vì chưa thêm công việc nào!")

            elif selected_menu == 3:
                for jobs in task:
                    if jobs["Trạng thái"] == "Đã hoàn thành":
                        task.remove(jobs)
                print('Đã xóa tất cả các công việc đã hoàn thành!')

            elif selected_menu == 4:
                print("Tạm biệt!")
                is_editing = False

            else:
                print("Đó là một lựa chọn không tồn tại")

            break

        except ValueError:
            print("Đã có lỗi! Hãy thử lại")