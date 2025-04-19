extern crate icns;

fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: {} <icns_file>", args[0]);
        std::process::exit(1);
    }

    let icns_filename = &args[1];

    if !icns_filename.ends_with(".icns") {
        println!("Error: The file must have a .icns extension");
        return;
    }
    let icns_path = std::path::PathBuf::from(&args[1]);
    let icns_file = std::fs::File::open(&icns_path).expect("Failed to open file");

    let icns_file_reader_obj = std::io::BufReader::new(icns_file);

    let icon_family =
        icns::IconFamily::read(icns_file_reader_obj).expect("Failed to read icns file");
    let &icon_type = icon_family
        .available_icons()
        .iter()
        .max_by_key(|icon_type| icon_type.pixel_width() * icon_type.pixel_height())
        .expect("No icons found in icns file");

    let png_path = icns_path.with_extension("png");
    let png_file = std::fs::File::create(png_path).expect("Failed to create png file");
    let output_image = icon_family
        .get_icon_with_type(icon_type)
        .expect("Failed to get icon");
    output_image
        .write_png(png_file)
        .expect("Failed to write png file");
}
