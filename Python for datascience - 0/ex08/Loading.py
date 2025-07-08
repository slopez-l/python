import sys
import shutil  # To get the terminal size


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, item in enumerate(lst, 1):
        # Get the current terminal width
        terminal_width = shutil.get_terminal_size().columns

        # Reserve space for fixed text: "100%|[bar]| 333/333"
        # Approximately 20 fixed characters (adjust if needed)
        fixed_space = len("100%|[]| 333/333")
        bar_len = max(10, terminal_width - fixed_space)

        # Calculate percentage and number of filled characters
        percentage = int((i / total) * 100)
        filled = int(bar_len * i // total)

        # Build the progress bar
        if i < total:
            bar = '=' * filled + '>' + ' ' * (bar_len - filled - 1)
        else:
            bar = '=' * bar_len

        # Print the progress bar on the same line
        sys.stdout.write(f"\r{percentage:3}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()

        yield item

    print()  # Newline at the end
