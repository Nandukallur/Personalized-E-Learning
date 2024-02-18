## basic diagram 1
# Import necessary libraries
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image

def generate_wordcloud(text, mask_image_path, output_path):
    # Load the mask image
    python_mask = np.array(Image.open(mask_image_path))

    # Create WordCloud with custom mask
    wc = WordCloud(stopwords=STOPWORDS, mask=python_mask, background_color="white",
                   contour_color="black", contour_width=3, min_font_size=3, max_words=100)

    # Generate the Word Cloud
    wc.generate(text)

    # Recolor the Word Cloud using the colors from the mask image
    colormap = ImageColorGenerator(python_mask)
    wc.recolor(color_func=colormap)

    # Save the Word Cloud image to a file
    wc.to_file(output_path)

    return wc


wordcloud = generate_wordcloud(text="Python Hello World Data Types Variables Operators OOPS Classes and Objects Inheritance Polymorphism Encapsulation Abstraction Control Flow Loops if ifelse elif while Lists Tuples Sets Dictionaries Lambda Functions File Handling Exception Handling Try, Except, Finally Regular Expressions Conditional Statements (if, elif, else) Arithmetic Operators Comparison Operators Logical Operators Bitwise Operators Assignment Operators Identity Operators Membership Operators import True False global",
                                mask_image_path=r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Personalized E-Learning\Personalized_E-Learning\Image.png",
                                output_path=r"C:/Users/shilp/OneDrive/Documents/Luminar/Internship/Personalized E-Learning/E_Learning/exam/static/images/wordcloud.png")



##basic diagram 2
import os
from graphviz import Digraph

# Add the path to the Graphviz bin directory to the system PATH
graphviz_path = r"C:\Program Files\Graphviz\bin"  # Update this with the correct path
os.environ["PATH"] += os.pathsep + graphviz_path

def create_tree_diagram():
    # Create a Digraph object
    dot = Digraph(comment='Tree Diagram', format='png', engine='dot')

    # Add nodes and edges for the tree structure
    dot.node('A', 'Data Types', shape='ellipse', style='filled', color='#306998', fontname='Pacifico', fontsize='30', fontcolor='white', penwidth='2')
    dot.node('B', 'Numeric', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontsize='28', fontcolor='black')
    dot.node('C', 'Text', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontsize='28', fontcolor='black')
    dot.node('D', 'Sequence', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontsize='28', fontcolor='black')
    dot.node('E', 'Mapping', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontsize='28', fontcolor='black')
    dot.node('F', 'Set', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontsize='28', fontcolor='black')
    dot.node('G', 'Boolean', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontsize='28', fontcolor='black')

    dot.node('H', 'int', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')
    dot.node('I', 'float', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')
    dot.node('J', 'complex', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')
    dot.node('L', 'list', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')
    dot.node('M', 'tuple', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')
    dot.node('N', 'range', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')
    dot.node('O', 'dict', shape='box', style='filled', color='#306998', fontname='Pacifico', fontsize='26', fontcolor='white')

    # Add edges
    dot.edges(['AB', 'AC', 'AD', 'AE', 'AF', 'AG'])
    dot.edges(['BH', 'BI', 'BJ'])
    dot.edges(['DL', 'DM', 'DN'])
    dot.edges(['EO'])

    # Set graph attributes
    dot.attr(bgcolor='#f0f0f0', fontcolor='black')

    return dot

if __name__ == "__main__":
    # Create the tree diagram
    dot = create_tree_diagram()

# View the diagram (opens in the default viewer)
dot.view()



## Intermediate diagram 1
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

# Function to generate the plot for if-else
def generate_plot():
    fig, ax = plt.subplots()

    # Small ellipse shape
    ellipse1 = patches.Ellipse((0.3, 0.9), 0.1, 0.05, edgecolor='black', facecolor='darkblue')
    ax.add_patch(ellipse1)
    ax.text(0.3, 0.9, "...", ha='center', va='center', color='white', weight='bold')  # Adding text to the ellipse

    # Arrow from ellipse to diamond
    arrow1 = patches.ConnectionPatch((0.3, 0.875), (0.3, 0.800), 'data', 'data', arrowstyle='->', linewidth=1, color='black', mutation_scale=15)
    ax.add_patch(arrow1)

    # Smaller diamond shape
    diamond = patches.RegularPolygon((0.3, 0.7), numVertices=4, radius=0.1, edgecolor='black', facecolor='blue')
    ax.add_patch(diamond)
    ax.text(0.3, 0.7, "Condition", ha='center', va='center', color='white', weight='bold')  # Adding text to the diamond

    # Arrow from diamond to rectangle
    arrow2 = patches.ConnectionPatch((0.3, 0.6), (0.3, 0.4), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow2)
    ax.text(0.2, 0.5, "When the if\nCondition is\nFalse", ha='center', va='center', color='black')  # Adding text to the left of arrow2

    # Line from diamond edge to the right
    line_from_diamond = lines.Line2D([0.4, 0.65], [0.7, 0.7], linewidth=1, color='black')
    ax.add_line(line_from_diamond)

    # Arrow from the line to the new rectangle in downward direction
    arrow_downward = patches.ConnectionPatch((0.65, 0.7), (0.65, 0.5), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow_downward)
    ax.text(0.75, 0.6, "When the if\nCondition is\nTrue", ha='center', va='center', color='black')  # Adding text to the right of arrow_downward

    # Rectangle shape with increased width
    rectangle1 = patches.Rectangle((0.2, 0.3), 0.2, 0.1, edgecolor='black', facecolor='blue')
    ax.add_patch(rectangle1)
    ax.text(0.3, 0.35, "else Block", ha='center', va='center', color='white', weight='bold')  # Adding text to the rectangle

    # Arrow from rectangle1 to ellipse
    arrow3 = patches.ConnectionPatch((0.3, 0.3), (0.3, 0.175), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow3)

    # Small ellipse shape (same size as the first one)
    ellipse2 = patches.Ellipse((0.3, 0.15), 0.1, 0.05, edgecolor='black', facecolor='darkblue')
    ax.add_patch(ellipse2)
    ax.text(0.3, 0.15, "...", ha='center', va='center', color='white', weight='bold')  # Adding text to the second ellipse

    # Rectangle to the right, slightly above
    rectangle2 = patches.Rectangle((0.55, 0.4), 0.2, 0.1, edgecolor='black', facecolor='blue')
    ax.add_patch(rectangle2)
    ax.text(0.65, 0.45, "if Block", ha='center', va='center', color='white', weight='bold')  # Adding text to the second rectangle

    # Line from rectangle2 to downward
    line_downward = lines.Line2D([0.65, 0.65], [0.4, 0.23], linewidth=1, color='black')
    ax.add_line(line_downward)

    # Arrow from line_downward to the left
    arrow_left = patches.ConnectionPatch((0.65, 0.23), (0.3, 0.23), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow_left)

    plt.axis('off')

    # Save the figure as an image
    fig.savefig(r'C:\\Users\\shilp\\OneDrive\\Documents\\Luminar\\Internship\\Personalized E-Learning\\E_Learning\\exam\static\\images\\ifelse.png')

# Call the function to generate the plot and save the image
generate_plot()




## Intermediate diagram 2
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Function to generate the plot for for-loop
def draw_flowchart():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Ellipse
    ellipse = patches.Ellipse((0.5, 0.85), 0.28, 0.2, fill=True, edgecolor='black', facecolor='green')
    ax.add_patch(ellipse)
    ax.text(0.5, 0.85, 'Start', ha='center', va='center', color='white', weight='bold')  # Add text to the center of the ellipse

    # Diamond shape with corrected orientation, filled with yellow
    diamond = patches.RegularPolygon((0.5, 0.525), numVertices=4, radius=0.13, orientation=0, fill=True, edgecolor='black', facecolor='yellow')
    ax.add_patch(diamond)
    ax.text(0.5, 0.525, 'Condition', ha='center', va='center', color='black', weight='bold')  # Add text to the center of the diamond

    # Larger Parallelogram, filled with blue
    parallelogram = patches.Polygon([(0.35, 0.3), (0.6, 0.3), (0.7, 0.18), (0.45, 0.18)],
                                    closed=True, fill=True, edgecolor='black', facecolor='blue')
    ax.add_patch(parallelogram)
    ax.text(0.525, 0.24, 'Statements', ha='center', va='center', color='white', weight='bold')  # Add text to the center of the parallelogram

    # Rectangle to the right and just above the parallelogram, filled with violet
    rectangle = patches.Rectangle((0.75, 0.33), 0.2, 0.12, fill=True, edgecolor='black', facecolor='violet')
    ax.add_patch(rectangle)
    ax.text(0.85, 0.39, 'Update', ha='center', va='center', color='black', weight='bold')  # Add text to the center of the rectangle

    # Connection patch from ellipse to diamond
    arrow1 = patches.ConnectionPatch((0.5, 0.77), (0.5, 0.63), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow1)

    # Connection patch from diamond to parallelogram
    arrow2 = patches.ConnectionPatch((0.5, 0.418), (0.5, 0.28), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow2)

    # Add "True" text to the right of arrow2
    ax.text(0.525, 0.35, 'True', ha='left', va='center', color='black', weight='bold')

    # Arrow from right to left starting from the right side of the diamond
    arrow3 = patches.ConnectionPatch((0.865, 0.525), (0.615, 0.525), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow3)

    # Connection patch upwards from the right side of the rectangle
    arrow_up = patches.ConnectionPatch((0.85, 0.23), (0.85, 0.35), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow_up)

    # Line upwards from the right side of the rectangle
    ax.plot([0.85, 0.85], [0.45, 0.525], color='black', linewidth=1)  # Adjust linewidth as needed
    ax.plot([0.645, 0.85], [0.25, 0.25], color='black', linewidth=1)
    ax.plot([0.15, 0.37], [0.525, 0.525], color='black', linewidth=1) 

    # Ellipse to the left of parallelogram below it
    ellipse_left_parallelogram = patches.Ellipse((0.15, 0.25), 0.28, 0.2, fill=True, edgecolor='black', facecolor='red')
    ax.add_patch(ellipse_left_parallelogram)
    # ax.plot([0.15, 0.15], [0.35, 0.525], color='black', linewidth=1) 
    arrow_end = patches.ConnectionPatch((0.15, 0.54), (0.15, 0.33), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow_end)

    ax.text(0.15, 0.25, 'End', ha='center', va='center', color='white', weight='bold')  # Add text to the center of the ellipse

    # Text "False" on the left side of the line from the diamond
    ax.text(0.3, 0.55, 'False', ha='right', va='center', color='black', weight='bold')

    # Set axis limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove axes for clarity
    ax.axis('off')

    # Save the figure to a file
    fig.savefig(r'C:\\Users\\shilp\\OneDrive\\Documents\\Luminar\\Internship\\Personalized E-Learning\\E_Learning\\exam\static\\images\\for-loop.png')

# Call the function to generate the plot
draw_flowchart()




## Intermediate diagram 3
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Function to generate the plot for while-loop
def draw_flowchart1():
    # Create figure and axes
    fig, ax = plt.subplots()

    # Create ellipse and fill with green
    ellipse = patches.Ellipse((0.3, 0.88), 0.4, 0.2, edgecolor='black', facecolor='green')
    ax.add_patch(ellipse)

    # Create arrow pointing downward
    arrow = patches.FancyArrowPatch((0.3, 0.78), (0.3, 0.67), color='black', mutation_scale=15, arrowstyle='->')
    ax.add_patch(arrow)

    # Create diamond shape at the arrowhead, fill with yellow, and set border color to black
    diamond = patches.RegularPolygon((0.3, 0.5), numVertices=4, radius=0.17, orientation=np.deg2rad(45), facecolor='yellow', fill=True, edgecolor='black')
    ax.add_patch(diamond)

    # Create arrow pointing downward from the bottom of the diamond
    arrow_below_diamond = patches.FancyArrowPatch((0.3, 0.33), (0.3, 0.24), color='black', mutation_scale=15, arrowstyle='->')
    ax.add_patch(arrow_below_diamond)

    # Create ellipse at the bottom of the second arrow and fill with red
    ellipse_below_arrow = patches.Ellipse((0.3, 0.14), 0.4, 0.2, edgecolor='black', facecolor='red')
    ax.add_patch(ellipse_below_arrow)

    # Create parallelogram to the right and above the diamond and fill with blue
    parallelogram = patches.Polygon(np.array([[0.6, 0.6], [0.9, 0.6], [1.0, 0.4], [0.7, 0.4]]), edgecolor='black', facecolor='blue')
    ax.add_patch(parallelogram)

    # Add a line starting from the center of the first arrow to the right
    line_x = [0.3, 0.75]  # X-coordinates for the line
    line_y = [0.75, 0.75]  # Y-coordinates for the line
    ax.plot(line_x, line_y, color='black', linewidth=2)

    # Draw a line from the parallelogram to upwards
    line_parallelogram_x = [0.75, 0.75]  # X-coordinates for the line
    line_parallelogram_y = [0.605, 0.75]   # Y-coordinates for the line
    ax.plot(line_parallelogram_x, line_parallelogram_y, color='black', linewidth=2)

    # Draw an arrow from the right edge of the diamond to the left side of the parallelogram
    arrow_diamond_to_parallelogram = patches.FancyArrowPatch((0.3 + 0.17, 0.5), (0.65, 0.5), color='black', mutation_scale=15, arrowstyle='->')
    ax.add_patch(arrow_diamond_to_parallelogram)

    # Add text to the patches
    ax.text(0.3, 0.88, 'Start', ha='center', va='center', color='black', fontsize=10, weight='bold')
    ax.text(0.3, 0.5, 'Condition', ha='center', va='center', color='black', fontsize=10, weight='bold')
    ax.text(0.3, 0.14, 'End', ha='center', va='center', color='black', fontsize=10, weight='bold')
    ax.text(0.8, 0.5, 'Statement', ha='center', va='center', color='black', fontsize=10, weight='bold')

    # Add text 'True' just above the line joining diamond and parallelogram
    ax.text(0.55, 0.53, 'True', ha='center', va='center', color='black', fontsize=10)

    # Add text 'False' to the right of the second arrow
    ax.text(0.32, 0.3, 'False', ha='left', va='center', color='black', fontsize=10)

    # Turn off the axis box
    ax.set_axis_off()

    # Set aspect ratio to 'equal' for a more accurate representation
    ax.set_aspect('equal', adjustable='box')

    # Specify the save path in Downloads folder
    save_path = r'C:\\Users\\shilp\\OneDrive\\Documents\\Luminar\\Internship\\Personalized E-Learning\\E_Learning\\exam\static\\images\\while-loop.png'

    # Save the plot as an image file
    plt.savefig(save_path, bbox_inches='tight')

# Call the function to generate, display, and save the flowchart
draw_flowchart1()




## advanced diagram 1
import matplotlib.pyplot as plt
import numpy as np

def draw_flower():
    num_petals = 6
    central_radius = 2.5
    surrounding_radius = 1.0
    distance = 5.0

    angle = np.linspace(0, 2 * np.pi, 100)

    central_x = central_radius * np.cos(angle)
    central_y = central_radius * np.sin(angle)
    plt.plot(central_x, central_y, color='purple')

    text_x = 0
    text_y = 0
    plt.text(text_x, text_y, "PYTHON", color='black', ha='center', va='center', fontsize=12, fontweight='bold')

    texts = ["Data Science", "Web\nDevelopment", "Game\nDevelopment", "Desktop GUIs", "Web Scraping", "CAD"]
    colors = plt.cm.viridis(np.linspace(0, 1, num_petals))

    for i in range(num_petals):
        x = (surrounding_radius + distance) * np.cos(i * (2 * np.pi / num_petals))
        y = (surrounding_radius + distance) * np.sin(i * (2 * np.pi / num_petals))
        plt.plot(x + central_x, y + central_y, color=colors[i], linestyle='--')

        text_x = x
        text_y = y
        text_color = colors[i]
        plt.text(text_x, text_y, texts[i], color=text_color, ha='center', va='center', fontsize=8)

    plt.axis('equal')
    plt.axis('off')
    
    # Specify the save path in Downloads folder
    save_path = r'C:\\Users\\shilp\\OneDrive\\Documents\\Luminar\\Internship\\Personalized E-Learning\\E_Learning\\exam\static\\images\\python-applications.png'

    # Save the plot as an image
    plt.savefig(save_path, bbox_inches='tight')

    # Return the Matplotlib figure
    return plt.gcf()

# Call the function to draw the flower and save it as an image
draw_flower()




##advanced diagram 2
import matplotlib.pyplot as plt
import numpy as np

def create_oo_plot():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(7, 7))

    # Draw a larger circle in the center with shadow
    circle_center = plt.Circle((0, 0), 0.3, edgecolor='black', facecolor='gray', lw=2, alpha=0.5)
    ax.add_patch(circle_center)

    # Draw lines radiating from the circumference with text boxes at the end and shadows
    num_lines = 6
    theta_values = np.linspace(0, 2 * np.pi, num_lines, endpoint=False)
    line_length = 0.5  # Adjusted line length

    box_labels = ['Class', 'Object', 'Encapsulation', 'Polymorphism', 'Inheritance', 'Abstraction']

    for i, theta in enumerate(theta_values):
        x = 0.3 * np.cos(theta)
        y = 0.3 * np.sin(theta)

        # Coordinates for the end of the line
        end_x = x + line_length * np.cos(theta)
        end_y = y + line_length * np.sin(theta)

        # Plot the shadow of the line
        ax.plot([x, end_x], [y, end_y], color='gray', lw=2, alpha=0.5)

        # Plot the line
        ax.plot([x, end_x], [y, end_y], color='black', lw=2)

        # Add a text box at the end of the line with a label and increased box size
        label = f'{box_labels[i]}'

        # Add a shadow for the text box
        ax.text(end_x + 0.07, end_y - 0.07, label, ha='center', va='center',
                bbox=dict(facecolor='gray', edgecolor='none', boxstyle='round,pad=2'), alpha=0.5)

        # Add the text box
        ax.text(end_x, end_y, label, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=2'))

    # Add the center text without a box
    ax.text(0, 0, 'Object\nOriented\nProgramming', ha='center', va='center', fontsize=14)

    # Set aspect ratio to be equal
    ax.set_aspect('equal', adjustable='box')

    # Remove axes for a cleaner look
    ax.axis('off')
    
    # Specify the save path in Downloads folder
    save_path = r'C:\\Users\\shilp\\OneDrive\\Documents\\Luminar\\Internship\\Personalized E-Learning\\E_Learning\\exam\static\\images\\oops.png'

    # Save the plot as an image
    plt.savefig(save_path, bbox_inches='tight')

    return fig

# Call the function to create the plot and save it
create_oo_plot()