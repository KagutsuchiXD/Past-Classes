import sys

LOREM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ultrices dui sapien eget mi proin sed libero. Metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices. Nec sagittis aliquam malesuada bibendum arcu vitae elementum. Est placerat in egestas erat. Egestas congue quisque egestas diam in. Erat nam at lectus urna. Faucibus turpis in eu mi bibendum neque. Amet dictum sit amet justo donec. Enim praesent elementum facilisis leo vel fringilla est ullamcorper. Et malesuada fames ac turpis egestas integer eget aliquet. Bibendum enim facilisis gravida neque. Gravida neque convallis a cras semper auctor neque vitae. Enim eu turpis egestas pretium aenean pharetra. Eu tincidunt tortor aliquam nulla facilisi cras. Eget duis at tellus at urna condimentum mattis pellentesque id.
Habitant morbi tristique senectus et netus et malesuada fames. Mi proin sed libero enim sed faucibus turpis. Et malesuada fames ac turpis egestas integer eget aliquet nibh. Eget dolor morbi non arcu risus quis varius. Eget gravida cum sociis natoque penatibus et. Id volutpat lacus laoreet non. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Pharetra vel turpis nunc eget lorem dolor. Facilisis volutpat est velit egestas dui id ornare. Gravida neque convallis a cras semper. Sed faucibus turpis in eu mi bibendum neque egestas congue. Lectus urna duis convallis convallis.
Iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui. Ante metus dictum at tempor commodo ullamcorper a lacus vestibulum. Eget nullam non nisi est. Egestas quis ipsum suspendisse ultrices gravida dictum. Praesent semper feugiat nibh sed pulvinar proin gravida hendrerit. Proin nibh nisl condimentum id venenatis a condimentum vitae sapien. Leo vel orci porta non pulvinar. Dignissim enim sit amet venenatis urna cursus eget nunc. In fermentum posuere urna nec tincidunt praesent. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae. Egestas dui id ornare arcu odio ut. Proin nibh nisl condimentum id venenatis a condimentum.
Sed cras ornare arcu dui vivamus. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Purus semper eget duis at tellus at. Dolor sit amet consectetur adipiscing elit ut aliquam purus sit. Mi eget mauris pharetra et ultrices neque ornare. Maecenas pharetra convallis posuere morbi. Elit duis tristique sollicitudin nibh. Sed tempus urna et pharetra pharetra massa massa ultricies mi. Condimentum id venenatis a condimentum vitae sapien pellentesque. Et molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Nisl pretium fusce id velit ut tortor. Gravida neque convallis a cras.
Nullam vehicula ipsum a arcu. Diam sollicitudin tempor id eu. Sed viverra ipsum nunc aliquet bibendum enim. Neque vitae tempus quam pellentesque nec. Dolor sit amet consectetur adipiscing. Pulvinar elementum integer enim neque volutpat ac tincidunt. Enim sed faucibus turpis in eu mi bibendum neque egestas. Augue ut lectus arcu bibendum at. Porttitor leo a diam sollicitudin tempor id eu nisl nunc. Tempus egestas sed sed risus pretium quam vulputate. Lectus urna duis convallis convallis tellus id interdum velit."""


name = sys.argv[1]

while True:
	print(f"Writer '{name}' attempts to open lorem.txt for writing...")
	f = open("lorem.txt", mode="w")
	for line in LOREM.split("\n"):
		for word in line.split():
			word = word.strip()
			print(f"{word} ", file=f)
			print(f"Writer '{name}' wrote the word {word}")
		print(file=f)
	f.close()

	
