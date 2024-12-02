from django.shortcuts import render
from django.http import HttpResponseRedirect

db_file = '/Users/gilart/Desktop/Try/Python/dict_of_words/dictsite/mainapp/words_dict.txt' 

# Функция для чтения данных из файла
def read_from_file():
    file = open(db_file, 'r', encoding='utf-8').read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        if line:
                word1, word2 = line.split(' - ')
                words1.append(word1)
                words2.append(word2)
        else: 
                continue
    return words1, words2
    

# Функция для добавления данных в файл
def add_to_file(word1: str, word2: str):
    with open(db_file, "a", encoding='utf-8') as file:
        file.write(word1.capitalize() + ' - ' + word2.capitalize() + '\n')
                

# Функция для поиска слова 
def search_word_in_file(search_word: str):
    word_found = False
    first_word_arr = []
    seconds_words_arr = []
    search_word_ed = search_word.strip().capitalize() # Удаляем лишние пробелы и приводим к регистру
    
    with open(db_file, "r", encoding='utf-8') as file:
        for line in file:
            if search_word_ed not in line: 
                seconds_words_arr.append(line)
            else:
                first_word_arr.append(line)
                word_found = True
    
    true_arr = first_word_arr + seconds_words_arr
    
    with open(db_file, 'w', encoding='utf-8') as file:
        for words in true_arr:
            file.write(words)          
    
    if word_found:
        word1, word2 = first_word_arr[0].strip().split(' - ')
        if search_word_ed == word1:
            return f'Слово {word1} переводится как {word2}'
        elif search_word_ed == word2:
            return f'Слово {word2} переводится как {word1}'
    else:
        return f'Слово {search_word_ed} не найдено!'
      

# Функция для удаления слова 
def delete_word_in_file(delete_word: str):
    word_found = False
    delete_word_ed = delete_word.strip().capitalize()
        
    with open(db_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    with open(db_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if delete_word_ed not in line.capitalize():
                file.write(line)   
            else:
                word_found = True
    
    if word_found:
        return f'Слово {delete_word} удалено!'
    return f'Слово {delete_word} не найдено!'
    

# Функция для редактирования слова 
def edit_word_in_file(old_word: str, edit_word: str):
    words_arr = []
    word_found = False
    old_word_ed = old_word.strip().capitalize()
    edit_word_ed = edit_word.strip().capitalize()
        
    with open(db_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
                
            for line in lines:
                    if old_word_ed not in line:
                            words_arr.append(line.strip())
                    else:
                            word_found = True
                            word1, word2 = line.strip().split(' - ')
                            if word1.capitalize() == old_word_ed:
                                    words_arr.append(f'{edit_word_ed} - {word2.capitalize()}')
                            elif word2.capitalize() == old_word_ed:
                                    words_arr.append(f'{word1.capitalize()} - {edit_word_ed}')
        
    with open(db_file, 'w', encoding='utf-8') as file:
            for el in words_arr:
                    file.write(f'{el} \n')
                           
    if word_found:
            return f'Слово {old_word_ed} изменено на {edit_word_ed}'
    else:
            return f'Слово {old_word_ed} не найдено!'
                                

# Топ 5 слов:
def last_five_words_for_searching():
    words_arr = []
    with open(db_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            words_arr.append(line.strip()) 
    
    return words_arr[:5]
        



# Отображение домашней страницы
def home_page(req):
    first_five_words = last_five_words_for_searching()
    
    return render(req, 'home.html', {'first_five_words': first_five_words})


# Отображения страницы со списком добавленных слов из файла
def show_words_page(req):
    if req.method == 'GET':
        words1, words2 = read_from_file()
        # Создаём список словарей, чтобы удобнее было работать в шаблоне
        words = [{'word': word1, 'translation': word2} for word1, word2 in zip(words1, words2)]
        return render(req, 'word_list.html', {'words': words})


# Страница для добавления новых слов
def add_word_page(req):
    if req.method == 'POST':
        add_to_file(req.POST['word1'], req.POST['word2'])
        return HttpResponseRedirect('/')
    return render(req, 'add_word.html')


# Поиск слова в словаре 
def search_word_page(req):
    result = None
    if req.method == 'POST':
        search_word = req.POST.get('search_word', '') # Получаем слово из формы
        result = search_word_in_file(search_word)
    return render(req, 'home.html', {'result': result}) # Передаём результат в шаблон


# Удаление слова из словаря 
def delete_word_page(req):
    result = None
    if req.method == 'POST':
        deleted_word = req.POST.get('deleted_word', '') # Получаем слово из формы
        result = delete_word_in_file(deleted_word)
    return render(req, 'delete_word.html', {'result': result}) # Передаём результат в шаблон

# Редактироване слова в словаре 
def edit_word_page(req):
    result = None
    if req.method == 'POST':
        old_word = req.POST.get('old_word', '')
        edited_word = req.POST.get('edited_word', '')
        
        result = edit_word_in_file(old_word, edited_word)
    return render(req, 'edit_word.html', {'result': result})

# Топ 5 последних искомых слов 
def last_five_words_page(req):
    if req.method == 'GET':
        first_five_words = last_five_words_for_searching()
        return render(req, 'home.html', {'first_five_words': first_five_words})
        
