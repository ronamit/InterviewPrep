def transform_points(H, points):
    """
    A function that takes a 3x3 homography and an array of points
    and returns the points after performing transformation
    :param H: 3x3 homography matrix (numpy array)  y = H * x
    :param points: Nx2 points (numpy array)
    return Nx2 points after applying homography (numpy array)
    """
    N = points.shape[0]
    points_ex = np.concat([points, ones(N, 1)], dim=1)  # Nx3
    points_h = points_ex @ H.T  # Nx3
    eps = 1e-10
    points_h = points_h / (points_h[:, 2] + eps)
    return points_h[:, :2]


def apply_forward_mapping(H, image):
    """
    A function that takes a 3x3 homography and an array of points
    and returns the points after performing transformation
    :param H: 3x3 homography matrix (numpy array)
    :param image: HxWx3 RGB image (numpy array)
    """
    H, W, n_chanels = image.shape
    points = [(h, w) for h in range(H) for w in range(w)]
    N = H * W
    points_hom = transform_points(H, points)
    h_min = points_hom[:, 0].min()
    h_max = points_hom[:, 0].max()
    w_min = points_hom[:, 1].min()
    w_max = points_hom[:, 1].max()
    H_n = h_max - h_min + 1
    W_n = w_max - w_min + 1
    image_n = np.zeros((H_n, W_n, 3))
    for i in range(N):
        h, w = points[i]
        colors = image[h, w, :]
        h_n, w_n = points_hom[i]
        h_n = np.round(h_n - h_min)
        w_n = np.round(w_n - h_min)
        image_n[h_n, w_n] = colors
    return image_n



