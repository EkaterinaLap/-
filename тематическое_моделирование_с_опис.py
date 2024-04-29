# -*- coding: utf-8 -*-
"""тематическое моделирование с опис.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ul85kVk1qCt9KeuEm2Ty5ROgAfim7MI2
"""

# Примеры отзывов
reviews_list = ['требую продолжения хочу ещё хочу 3 4 5 литературная основа позволяет бюджет окупится дайте нам продолжение банкета первая часть фильма вызвала множество негативных откликов люди которых голова формой крутое яйцо объяснили нам литературы кинематографа разные языки всё книге перенести экран вильнёв интерпретирует герберта интерпретирую вильнёва интерпретируй интерпретаторов фильме хорошего надсадно хрипло демонически захохотать шаламе многие упрекали одинаковое выражение лица протяжении фильма понимаю почему вильнёв взял роль пола муад диба лисан гайиба квисац хадерача это просто логопедическое упражнение какое мальчика это касса фильм должны посмотреть мальчики девочки денежки принесут шаламе небрежной мальчишеской красотой искусно растрепанными волосами грустным ликом глазами слезой идеальная приманка мечтательных девиц требовался актёр мальчик хрупкий внешне обладающий скрытой внутренней силой герой шаламе претерпевает метаморфозы сомневается боится колеблется видим выкристаллизовывается характер пол проходит путь инфантильного сынка знатного папаши религиозному лидеру руководителю революции речь вождями южных племен слушать перевода та редкая шерсть которая растет загривке сих пор стоит дыбом словах фильма выдуман свой язык содержится энергия взрывной силы хочется схватить зуб шей хулуда балисет сковородку стакан водки простите увлеклась хочется схватить бежать свергать харконенов шаламе очень хорош съёмки грандиозные чарующие волшебные виды закатной пустыни снятые тёплых ласкающих глаз золотистых тонах масштабные спецэффекты гигантские черви носятся пустыне поезда московских диаметров красиво горящие гравицапы харконенов парады своим гигантизмом напоминающие воли лени рифеншталь эпические сцены битв взрывы амфитеатр харконенов отсылка гладиаторским боям часто думаете римской империи учитесь осваивать бюджет фильма изобретён специальный язык шаламе разработали походку стиле полотёр позволяющую передвигаться пустыне привлекая внимания червей снялись кристофер уокен огромные печальные глаза седой пух грязноликий бардем романтичный романс моче бролин приманка мальчиков зандея многие другие предвосхищаю реплики перфекционистов вильнев выкинул линию ментатов полностью зря это целая философия необычная увлекательная отсутствует борьба власть внутри клана харконенов книжный фейд раута искусный интриган манипулятор садист пытающийся помощью ментатов угробить любимого дядю вову харконена фильме фейд просто садист западные критики восхищаются игрой остина батлера впечатлил бритый череп гидроцефала немигающий взгляд исподлобья сжатые хруста крошащихся зубов челюсти отсутствие эмоций ведёт любой киносоциопат начиная ганнибалом лектором заканчивая злобной мышью томом джерри страдает наслаждается вильнёв шизофренией одном кадров пол спрашивает чани стилгар научит ездить черве чани отвечает коем случае фримен следующий кадр стилгар гонит пола пустыню оседлай шей хулуда чани восторгом стилгар тренировал пол верхом черве выглядит московский мэр открытии очередной станции метро пыли пафоса свист ветра ушах сле тель леди джессика выпивает синенького денатурату бац следующем кадре её лицо покрыто какими каракулями автографы участников отравления инструктаж технике безопасности те осилил книгу могут понять почему лицо бардема становится грязнее каждым кадром бережёт влагу тела поняла фильм экологию эксплуатация ресурсов борьбу севера юга харконены арийцы бритыми головами набеленными лицами фримены обладают характерными арабов профилями бородами знаете гербертом азимовым шло негласное соревнование оба фантаста историческими оптимистами оба уверены неизбежной гибели планеты азимов пишет цикл книг которых предлагает выход сохранить цивилизацию помощью науки герберт создаёт предлагает свой вариант спасения религия махди джихад термины имеющие конкретные коннотации природе власти механизмах влияния сознание управляемых революции устроенной аристократом атрейдисом помощью пролетариев пустыни фрименов империи бессмертны могут менять формы изменяться времени пространстве суть остаётся имперскость пробухаешь детерменизме пол состоянии изменить должен править последствия будут чудовищными случае отказа ещё хуже выбор это иллюзия искусно наведённый морок специя позволяет видеть будущее позволяет изменить итог прекрасное кино недостатки которого выгодно оттеняют достоинства',
 'часа красивых картинок дени вильнева часто упрекают уделяет форме внимания содержанию дюна 2 наиболее яркий пример недостатка первой части легко показывай зрителю красивые миры тебе успех второй части хочется узнать подробностей хитросплетениях политики империи главных героях жизни фрименов дени вильнев сожалению плохой рассказчик сильный перекос сторону визуала добиться нужного эффекта картинки доводит характеры персонажей крайности выходе получаем невменяемых харконненов которые своих приближенных ужин готовят злобную стерву джессику жаждущую сделать сына мессию любой ценой одержимого фанатика стилгара прошлого фильма изменившегося неузнаваемости глядя клоунаду фраза планы внутри планов звучит насмешка интриг уровня игры престолов явно вышло зато картинка красивая реализму происходящего отдельный вопрос живут фримены своих пещерах остается загадкой люди обносках едят полу беженцы продвинутые технологии имеются кроме нового жизни часа узнала императора жизнь скромна правит дочерью одну руку ясновидящей бене гессерит другую видимо управлять вселененной никого другие дома министры ау временами фильм похож музыкальный клип череда красивых абстрактных образов примитивные диалоги дело звучат банальные пустые фразы вместо полноценных интересных разговоров взрослыми наделенными властью людьми очень разочарована фильмом особенно фоне удачной кажется первая часть просидела кинотеатре часа получила эпичной битвы конце раскрытия персонажей сюжета сравнения 6 часов властелина колец узнаем живут вселенной хоббиты люди волшебники орки энты успеваем пройти полмира мощную битву конце хватает времени наполнил свои часы дени вильнев поскольку пришел документального кино здорово умеет показать настоящий момент поэтому например сцена пол оседлал червя убеждал фрименов сражаться выглядят очень моменты ощущаются живо осязаемо вызывают яркие эмоции также мастерски умеет создать атмосферу таинственности опасности плане понравились эпизоды остин батлер здорово сыграл персонажа передавая всем телом смертельно опасную грацию актерский состав целом блестящий очень понравилось тимоти шаламе сыграл агрессию становление лидера увидела новую грань таланта актера недостаточно итогу весь фильм видится серия разрозненных эпизодов готовящих эпичной кульминации которой произошло лишнего стоило вырезать недостающего добавить баланса драматизмом зрелищностью глубиной истории описанием повседневности стороны вильнев передал основную мысль книг герберта умел стоило делать трехчасовой фильм думаю',
 'дюна картинок звука мало скажу сразу книгу читал первый фильм понравился просмотра 2 части смотря минусы понимаю фильм должен полностью повторять книгу хотел интересный фильм 2 часа 40 минут картинок музыку экранизация книг дело опасное экранизация популярных фэнтезийных книг дело крайне опасное сложное пока одного режиссера удалось провернуть это дело ударив грязь лицом местами превзойти первоисточник накалу эпоса спасибо питеру джексону властелина колец обычно сводится тому процессе работы сценарием создатели вырезают картины самые интересные сюжетные ходы заменяя своими фантазиями вперемешку современными трендами именно это случилось дюной первый фильм снимали опираясь книгу соблюдая внутренние законы вселенной дюны второй фильм снимался статье википедии соблюдая законы лора игнорируя местами первую часть упрощение упростили нам сложные переживания пола антрейдеса который став большим человек обретя дар видеть будущее стоит сложным выбором череды событий нам сложные рассуждения религию судьбу это сложно современного зрителя дай бог обидится нам интриги заговоры гильдии навигаторов сестер бена гесерид которые прямо влияют финал истории поведение героев 2 часа 40 минут хронометража это хватить времени зритель понять запутаться этих сложных именах императора будем звать просто император шадам это созвучно садам могут плохие заполнить 2 часа 40 минут сильной независимой тчани исполнении зенадаи которая обладает удивительном актерским талантом своих фильмах играет одного персонажа это недовольный подросток который периодически употребляет поэтому хмурое снять очень пустыни экшена минут умные диалоги снимать пол атрейдес мессии сверхчеловека который способен видеть прошлое будущее обладающий огромной харизмой объединивший племена фрименов заменяется мальчишку которого интерес жизни это молодая девушка тчани тчани девушки которая всем поддерживала муадбида которая готова женой наложницей любви полу меняем персонажа которая обижается избранного хочет свободы игнорирование первого фильма личные щиты пропали зато появился нелепый паркур ножами который смотрится нелепо смешно почему просто взять лазер выжигать вся становится ясно сардаукары самых грозной силы превратились каких болванчиков которые е способы пропала гильдия навигаторов которая играет очень важную роль вселенной дюны никуда добраться путешествий космосу нужен спайс ценность планеты аракис ставится вопрос зато появились спутники аракисом хотя первой части нам сказали великие дома каким образом обзавелись кораблями межзвездных перелетов наверное захватили распущенной гильдии резко смогли финал вместо напряженного сложного финала фильма получили скомканную максимально упрощенную версию удаления фильма важных действующих персонажей мотивация поведение героев определятся лишь шаблонами любого месть император дочь нужны мебель сардаукары массовка харконенны лишь первой части дени вильнев любит красивую картинку звук дени вильнев снял красивую картинку звук назвать это фильмом назвать это кинопродуктом обезжиренным обездуховленным какого либо послевкусия 5 баллов прекрасную музыку ханса цимера красивые картинки оператора голливуд продолжает расстраивать кризис',
 'кропотливая работа матерей кончиках пальцев нереальном восторге нахожусь просмотра сложно описать ожидания просмотренный фильм оказался совершенно другим потрясающим воображение визуальную часть вижу смысла расписывать понятно ещё первой части вильнёв целом великолепный визионер сценарий отстаёт скажешь кэмероне вторая часть насыщена умными необычными решениями фишками отсылками очень порадовало преобладание светлых сцен саундтрек ханца переоценить сложно великолепен проектах подобного уровня касается сюжета рваный первой части избежать конце фильма вильнёв продолжает знакомить искушённого зрителя вселенной фрэнка герберта намекая хочет взяться следующую книгу говорил случае съёмки станет последней вселенной дюны считаю вильнёв согласен автором книги понимает видение мира грядущего толкин фрэнк герберт проецировал проблемы нашей жизни вселенную просмотра первой части огорчён практически видели сталгара исполнении хавьера бардема раскрыли полной мере играет великолепно стоит отметить практически персонажей введенных втором фильме вызвал отторжения скарсгард высоте фильмы книга демонстрируют реальность беспощадно жёстко сухо пески дюны править сердцем это слабость приходится делать тяжёлый выбор вильнёв демонстрирует вера религия важны мира ввести смуту одурачить слабых поразить сознания фанатиков предписаний просто грамотная планировка просмотр навсегда отложится памяти смог сходить imax ещё новой стране обязательно рекомендую просмотру кому понравилась первая часть кому значит жанр ваш второй части экшна 10 10',
 'рейтинг кинопоиске эээ это сравнению самобытным своему интересным запоминающимся первым фильмом развалился сути крайне затянутый фильм который совершенно необоснованно идёт часа которые экране происходит попросят пересказать сюжет этим будут трудности сюжет крайне плохо подан фильме нами набор разрозненных местами нелогичных сцен которые рассказывают интересную связную историю сожалению очень вопросов мотивации действиям персонажей раскрыто живут фримены едят моются ещё императорском дворе помимо троицы тронном зале главный герой оказывается харконнен вообще никак обыграна персонажи раскрытые некоторым явно мало времени это дали главный персонаж одинаковым лицом весь фильм ходит единственный проблеск света хавьер бардем стилгар леа сейду ещё постоянно выбивают погружения дурацкие сцены например почему освоили межпланетные перелёты бои ведутся средневековых ножах сложно оседлать червя почему нём катаются кому лень червей используют метро ещё туда ходу умудрились заскочить сотни людей ещё балдахин ведьмы закрепить блин слезают этих червей ходу графика ужасная возможно задумано зашло зайдёт военный марш духе третьего рейха буду удивлён это всё плохом давайте хорошем картинка пустыни привлекательная конце фильма прямой подвод третьей части пожалуйста продолжать',
 'пророк дюна часть вторая самых ожидаемых фильмов года говорить года несколько последних лет помню выходя кинотеатра 2021 года просмотра первой части таком восторге увиденного дюна сразу пополнила список моих любимых фильмов выход продолжения топе ожидания сюжету фильма пол атрейдес своей матерью джессикой следует вместе фрименами поселение освоить обычаи народа полу предстоит стать лидером часть фрименов верит пророк который приведёт победе матери пола предначертана важная сказать дюна часть вторая это шедевр полном восторге это живая история которой сбалансировано всё визуальная потрясающие сцены пустыне персонажи которые получили развитие ними действительно интересно наблюдать превосходный саундтрек ханса циммера который является украшением фильма задает атмосферу происходящего экране дени вильнёв проделал колоссальную работу чувствуется насколько вложено сил данный проект самое главное видно кино сделано душой фильме отличная операторская работа события фильма развиваются большую часть арракисе кругом пустыня этим совершенно скучно наблюдать фильме события происходят вполне динамично постепенно нагнетая финалу который пробирает мурашек актерах тимоти шаламе пол атрейдес персонаж протяжении фильма преображается чужака превращается миссию начале истории ещё сомнениях финалу становится лидером который поведёт собой фрименов тимоти сыграл эмоционально персонажу веришь переживаешь одной стороны сочувствуешь жалеешь приходится жертвовать личным имя обретения власти тимоти отлично передал изменение героя ребекка фергюсон джессика героиня кардинальным образом преобразуется становится преподобной матерью сути обретает влияние власть теми верит миссию джессика сравнению первой частью значительно меняется фергюсон образе убедительна зендея чани её героиня продолжении становится значимым персонажем помогает полу стать своим становится союзником возлюбленной хавьер бардем стилгар очень харизматичный персонаж получился который верит пол миссия стороне всём помогает остин батлер племянник барона харконнена напрочь сумасшедший персонаж который поражает своей жестокостью батлер образе несомненно хорош общем дюна часть вторая получился впечатляющим продолжение которое захватывает своим повествованием первой последней минуты визуальной точки зрения кино прекрасно отличная актёрская игра достойная операторская работа музыкальное сопровождение гениально надеюсь дени вильнёв вновь вернётся мир дюны завершит трилогию буду нетерпением',
 'красивая обертка стоит признать люблю вильнёва удивительное дело смотришь красивейший фильм восхитительным визуалом отличной большей части ниже подборкой актёров ждёшь закончится сути первую часть дюны смотрела понравилась шикарная ребекка фергюсон шаламе скарсгард хавьер бардем остались второй части добавилась флоренс пью качестве аристократичной величественной высокой принцессы ирулан всей любовью пью вытянула смыслах почему та аня присутствующая фильме сестра алия объективно подходящая выбрана роль ирулан многих зрителей любителей дюны загадка случись рокировка этих двух актрис фильм приятнее смотреть сюжет фильма всё красиво медленно немногословно стиле вильнёва дюна определённо требует широкого раскрытия формате кино часа наблюдаем виды прекрасную графику крупные планы очень важные ёмкие книжные диалоги которые заняли минимум экранного времени подчёркивающие сюжет отсутствуют прекрасно пожертвовать 15ю минутами безмолвных переглядок видов пользу объяснений знакомы миром дюны уловить суть картина останется скудной смотреть визуалам определённо дома кино',
 'желание отомстить приводит пола настоящей священной войне которой погибнет множество людей главный герой забывает принципах близких погоне властью пол теряет человеческий облик душу уподобившись своим врагам это главная тема дюны это предназначение человека пол мстить решил власти хапнуть увидел будущее принял судьбу',
 'красивый видеоряд сюжет вторая часть разорвана отдельные сцены единой связи сценами диалогами первая часть понравилась скажу скучно затянуто кстати сравнении книгой фильм лишен многих диалогов которые являются важными философскими фильм картинка пересмотрю разок возможно изменю свое мнение',
 'вышли кинотеатра фильм огонь часа выпали реальной жизни первой частью',
 'дюна одна самых переоцененных книг средневековое устройство общества 100 веков такое гамильтон звездных королях описывал маловато фантазии большинства фантастов лем исключение возможно вспомнить современном обществе феодальная аристократия полнейший анахронизм',
 'фильма читал трилогию пытался посмотреть фильм 1980 года очень впечатлился книгой ужас ждал случится чудо выйдет отличная экранизация ч первой части стало понятно это случилось вторая это вообще масштабище захватывающе интересно некоторых моментах зал просто останавливал дыхание момент подумалось давно такого эпичного вроде властелина колец 3 часа реально мало б длился жаль третью увидим скоро вовсе',
 'чушь подойдет качестве безмедикаментозного снотворного монотонные диалоги весь фильм приглушенным голосом отлично справляются задачей отправить человека глубокий сон минуте',
 'странное ощущение очень красиво совершенно цепляет примерно второй аватар задел третью часть священной войной виден озеленения арракиса трансформации червя дойдут',
 'нереально выбесила любовь протагониста вместо поддержки чувака который казалось топит народ пытается вести светлое будущее откровенно плюет какие народа альтернативы власти сгнить дюнах артой хардконеров акуеть просто это фемки представляют силу независимость скотство слабоумие отличная модель поведения надеюсь мразоту ждет 3 части жуткая неприятная смерть кстати мать главного героя показана раскрыта превосходно кого нужно равняться девушкам желающим сильными порадовал младший семейства харконеров мало времени уделено блин потрясающая актерская работа хз слов передать безумие холодный расчет просто одном взгляде боец гладиатор блин мое почтение общем целом фильмец зашел ждем продолжения отдельное спасибо этому медиа ресурсов качество натыкали рекламы видео ряд приятно посмотреть',
 'это самая сильная кино адаптация игры бесспорный шедевр музыка звук эффекты сюжет просто крышесносное зрелище смотрел одном дыхании думаю пола девушку ждут роковые события скорее следующей части пожертвует собой ради дени вильнев задрал планку качества duna очень высокий уровень дай бог последующие части оставались уровне просто кайфонул']
# Импортируем необходимые библиотеки sklearn и numpy для построения матрицы
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import numpy as np
# TfidfVectorizer() преобразовывает текст в матрицу TF-IDF, которая содержит информацию о ключевых словах и их частотности в отзывах
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(reviews_list)
# Задаем количество тем, которые будут извлекаться и преобразуем список отзывов в матрицу LSA
n_components = 16
lsa = TruncatedSVD(n_components)
lsa_matrix = lsa.fit_transform(tfidf_matrix)
# Извлекаем ключевые слова для каждой темы
terms = np.array(vectorizer.get_feature_names_out())
for i, topic in enumerate(lsa.components_):
    top_terms_idx = topic.argsort()[-5:][::-1]  # Получаем топ-5 слов в каждой теме
    top_terms = terms[top_terms_idx]
    print(f"Topic {i + 1}: {', '.join(top_terms)}")